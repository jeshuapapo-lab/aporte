import json, re, time
from pathlib import Path
import numpy as np
import soundfile as sf
import onnxruntime as ort
from kokoro_onnx import Kokoro
from contenido import *

SR=24000
OUT=BUILD/'audio'
OUT.mkdir(exist_ok=True)
opts=ort.SessionOptions();opts.intra_op_num_threads=3;opts.inter_op_num_threads=1
session=ort.InferenceSession(str(MODEL_DIR/'kokoro-v1.0.onnx'),sess_options=opts,providers=['CPUExecutionProvider'])

class TypedSession:
    """Adaptación al esquema real del modelo: kokoro-onnx 0.4.9 envía speed int32 en modelos input_ids."""
    def __getattr__(self,key):return getattr(session,key)
    def run(self,outputs,inputs):
        if 'speed' in inputs:
            expected=next(i.type for i in session.get_inputs() if i.name=='speed')
            if expected=='tensor(float)': inputs['speed']=np.asarray(inputs['speed'],dtype=np.float32)
        return session.run(outputs,inputs)

k=Kokoro.from_session(TypedSession(),str(MODEL_DIR/'voices-v1.0.bin'))

def synthesize(text,path,speed):
    cache=path.with_suffix('.json')
    if path.exists() and cache.exists():
        info=json.loads(cache.read_text())
        # El adaptador anterior y el actual usan efectivamente velocidad 1.0.
        info['speed']=1.0
        return info
    sections=re.split(r'(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÑ¿¡])',text)
    pieces=[np.zeros(int(.28*SR),dtype=np.float32)]
    cursor=.28;captions=[]
    for sentence in sections:
        a,sr=k.create(sentence,voice='ef_dora',lang='es-419',speed=float(speed))
        assert sr==SR and np.isfinite(a).all()
        # Normaliza solo atenuando picos anómalos. La sonoridad final se normaliza en FFmpeg.
        peak=float(np.max(np.abs(a)))
        if peak>.96:a=a*(.96/peak)
        dur=len(a)/SR
        captions.append({'start':cursor,'end':cursor+dur,'text':sentence})
        pieces.extend([a,np.zeros(int(.25*SR),dtype=np.float32)])
        cursor+=dur+.25
    pieces.append(np.zeros(int(.30*SR),dtype=np.float32))
    full=np.concatenate(pieces);sf.write(path,full,SR,subtype='PCM_16')
    info={'duration':len(full)/SR,'captions':captions,'voice':'ef_dora','language':'es-419','speed':speed,'words':len(text.split())}
    cache.write_text(json.dumps(info,ensure_ascii=False,indent=2),encoding='utf-8')
    return info

def srt_time(t):
    ms=round(t*1000);h,ms=divmod(ms,3600000);m,ms=divmod(ms,60000);s,ms=divmod(ms,1000)
    return f'{h:02}:{m:02}:{s:02},{ms:03}'

if __name__=='__main__':
    timeline=[];cursor=0
    for i,s in enumerate(SLIDES):
        start=time.time();info=synthesize(s['narration'],OUT/f'video_{i:02d}.wav',1.0)
        timeline.append({'index':i,'start':cursor,**info});cursor+=info['duration']
        print(f'Escena {i+1}: {info["duration"]:.1f}s, generación {time.time()-start:.1f}s',flush=True)
    combined=np.concatenate([sf.read(OUT/f'video_{i:02d}.wav',dtype='float32')[0] for i in range(len(SLIDES))])
    sf.write(OUT/'narracion_video.wav',combined,SR,subtype='PCM_16')
    captions=[]
    for s in timeline:
        for cap in s['captions']:
            # Segmentación proporcional en bloques de hasta 11 palabras para facilitar la lectura.
            # Son tiempos orientativos dentro de una frase sintetizada, no alineación fonética forzada.
            words=cap['text'].split();chunks=[words[j:j+11] for j in range(0,len(words),11)]
            total=sum(len(' '.join(x)) for x in chunks);pos=0
            for chunk in chunks:
                length=len(' '.join(chunk));start=s['start']+cap['start']+(cap['end']-cap['start'])*pos/total
                end=s['start']+cap['start']+(cap['end']-cap['start'])*(pos+length)/total
                captions.append({'start':start,'end':end,'text':' '.join(chunk)})
                pos+=length
    (OUT/'timeline.json').write_text(json.dumps({'scenes':timeline,'captions':captions,'duration':cursor},ensure_ascii=False,indent=2),encoding='utf-8')
    (TOPIC/'Subtitulos.srt').write_text('\n\n'.join(f'{i+1}\n{srt_time(c["start"])} --> {srt_time(c["end"])}\n{c["text"]}' for i,c in enumerate(captions))+'\n',encoding='utf-8')
    print(f'Duración video: {cursor:.1f} segundos',flush=True)
    audio=[]
    for i,p in enumerate(AUDIO_PARAGRAPHS):
        start=time.time();info=synthesize(p,OUT/f'podcast_{i:02d}.wav',1.0)
        audio.extend([sf.read(OUT/f'podcast_{i:02d}.wav',dtype='float32')[0],np.zeros(int(.55*SR),dtype=np.float32)])
        print(f'Audio párrafo {i+1}: {info["duration"]:.1f}s, generación {time.time()-start:.1f}s',flush=True)
    a=np.concatenate(audio);sf.write(OUT/'audio_independiente.wav',a,SR,subtype='PCM_16')
    print(f'Audio independiente completo: {len(a)/SR:.1f}s',flush=True)
