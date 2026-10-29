import concurrent.futures, json, math, subprocess, textwrap
import numpy as np
import soundfile as sf
from contenido import *

V=BUILD/'video';A=BUILD/'audio';V.mkdir(exist_ok=True)
FPS=24;SR=24000

def srt_time(t):
    ms=round(t*1000);h,ms=divmod(ms,3600000);m,ms=divmod(ms,60000);s,ms=divmod(ms,1000)
    return f'{h:02}:{m:02}:{s:02},{ms:03}'

def run(cmd):
    result=subprocess.run(cmd,capture_output=True,text=True)
    if result.returncode:raise RuntimeError(' '.join(cmd)+'\n'+result.stderr[-5000:])
    return result

def music(duration):
    n=math.ceil(duration*SR);a=np.zeros(n,dtype=np.float32)
    # Composición instrumental original: arpegios suaves de teclado, sin samples externos.
    chords=[[48,55,59,64],[45,52,55,60],[41,48,52,57],[43,50,57,62]]
    for k,start in enumerate(np.arange(0,duration,1.7)):
        notes=chords[(k//8)%len(chords)]
        midi=notes[k%4]+(12 if k%4>1 else 0);freq=440*2**((midi-69)/12)
        length=min(int(4.5*SR),n-int(start*SR));t=np.arange(length)/SR
        env=(1-np.exp(-t/.025))*np.exp(-t/1.15)
        tone=(np.sin(2*np.pi*freq*t)+.28*np.sin(4*np.pi*freq*t)*np.exp(-t/1.4)+.09*np.sin(6*np.pi*freq*t))*.7
        note=(tone*env).astype(np.float32);idx=int(start*SR);a[idx:idx+length]+=note
    # Eco breve a bajo nivel para un timbre más suave.
    for delay,gain in [(.18,.12),(.37,.06)]:
        shift=int(delay*SR);a[shift:]+=a[:-shift].copy()*gain
    rms=float(np.sqrt(np.mean(a*a)));a*=.014/max(rms,1e-9)
    fade=min(int(2*SR),n//2);a[:fade]*=np.linspace(0,1,fade);a[-fade:]*=np.linspace(1,0,fade)
    sf.write(A/'musica_original.wav',a,SR,subtype='PCM_16')

def ass_time(t):
    cs=round(t*100);h,cs=divmod(cs,360000);m,cs=divmod(cs,6000);s,cs=divmod(cs,100)
    return f'{h}:{m:02}:{s:02}.{cs:02}'

def ass(caps):
    header='''[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0
[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Noto Sans,38,&H00FFFFFF,&H00FFFFFF,&H003C2B11,&H003C2B11,0,0,0,0,100,100,0,0,1,1.5,0,2,180,180,45,1
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
'''
    for cap in caps:
        escaped=cap['text'].replace('{','').replace('}','')
        header+=f'Dialogue: 0,{ass_time(cap["start"])},{ass_time(cap["end"])},Default,,0,0,0,,{{\\fad(80,80)}}{escaped}\n'
    return header

def clip(scene):
    i=scene['index'];duration=scene['duration'];dst=V/f'{i:02d}.mp4'
    subtitle=V/f'{i:02d}.ass';subtitle.write_text(ass(scene['local_captions']),encoding='utf-8')
    filters=f"[0:v]pad=1920:1080:160:0:color=0x112B3C[base];color=c=0x087E8B:s=1600x6:r=24:d={duration:.6f}[bar];[base][bar]overlay=x='160-1600+1600*min(t/{duration:.6f},1)':y=914:shortest=1,drawbox=x=0:y=914:w=160:h=6:color=0x112B3C:t=fill,subtitles={subtitle},fade=t=in:st=0:d=0.28,fade=t=out:st={duration-.28:.6f}:d=0.28,format=yuv420p[v]"
    run(['ffmpeg','-hide_banner','-loglevel','error','-y','-loop','1','-framerate',str(FPS),'-i',str(BUILD/'slides'/f'{i:02d}.png'),'-filter_complex_threads','1','-filter_complex',filters,'-map','[v]','-t',str(duration),'-an','-c:v','libx264','-preset','veryfast','-crf','21','-threads','2','-r',str(FPS),str(dst)])
    print(f'Video escena {i+1} exportado: {duration:.2f}s',flush=True)
    return dst

if __name__=='__main__':
    timeline=json.loads((A/'timeline.json').read_text())
    scenes=timeline['scenes'];old=timeline['captions'];caps=[];audio=[];offset=0
    for scene in scenes:
        start=scene['start'];duration=scene['duration'];i=scene['index']
        samples,sr=sf.read(A/f'video_{i:02d}.wav',dtype='float32');assert sr==SR
        aligned=math.ceil(len(samples)/1000)*1000
        samples=np.pad(samples,(0,aligned-len(samples)))
        local=[{'start':c['start']-start,'end':c['end']-start,'text':c['text']} for c in old if c['start']>=start-1e-5 and c['start']<start+duration-1e-5]
        scene.update(start=offset,duration=aligned/SR,local_captions=local)
        caps.extend({'start':offset+c['start'],'end':offset+c['end'],'text':c['text']} for c in local)
        offset+=aligned/SR;audio.append(samples)
    assert 120<=offset<=240,offset
    sf.write(A/'voz_video_alineada.wav',np.concatenate(audio),SR,subtype='PCM_16')
    (TOPIC/'Subtitulos.srt').write_text('\n\n'.join(f'{i+1}\n{srt_time(c["start"])} --> {srt_time(c["end"])}\n{c["text"]}' for i,c in enumerate(caps))+'\n',encoding='utf-8')
    timeline.update(scenes=scenes,captions=caps,duration=offset)
    (V/'timeline_final.json').write_text(json.dumps(timeline,ensure_ascii=False,indent=2),encoding='utf-8')
    music(offset)
    run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',str(A/'voz_video_alineada.wav'),'-af','loudnorm=I=-16:TP=-2:LRA=7','-ar','48000','-c:a','pcm_s24le',str(A/'voz_normalizada.wav')])
    run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',str(A/'audio_independiente.wav'),'-af','loudnorm=I=-16:TP=-1.5:LRA=7','-ar','44100','-c:a','libmp3lame','-q:a','2','-metadata','title=Las páginas de inicio — explicación independiente','-metadata','artist=Proyecto educativo — voz sintética neuronal es-419',str(TOPIC/'Audio.mp3')])
    print('MP3 independiente exportado',flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        list(pool.map(clip,scenes))
    (V/'concat.txt').write_text('\n'.join(f"file '{V/f'{i:02d}.mp4'}'" for i in range(len(scenes)))+'\n',encoding='utf-8')
    mix='[1:a]asplit=2[voz][control];[2:a][control]sidechaincompress=threshold=0.05:ratio=5:attack=20:release=400[musica];[voz][musica]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.94:level=0[a]'
    run(['ffmpeg','-hide_banner','-loglevel','error','-y','-f','concat','-safe','0','-i',str(V/'concat.txt'),'-i',str(A/'voz_normalizada.wav'),'-i',str(A/'musica_original.wav'),'-filter_complex',mix,'-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k','-ar','48000','-t',str(offset),'-movflags','+faststart','-metadata','title=Las páginas de inicio — Negocios Electrónicos 1.1','-metadata','comment=Voz sintética neuronal con fonetización es-419. Música e ilustraciones originales. Caso y datos ficticios.',str(TOPIC/'Video.mp4')])
    print(f'MP4 final: {offset:.2f} segundos, 1920×1080, 24 fps, H.264 y AAC',flush=True)
