import sys,json,time,functools,http.server,threading
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT=Path('/workspace/Proyecto_Educativo_Completo');BASE=Path('/workspace/edu-full')
class Quiet(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(ROOT)))
threading.Thread(target=server.serve_forever,daemon=True).start()
base=f'http://127.0.0.1:{server.server_port}/'
errors=[]
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True)
 page=browser.new_page(viewport={'width':1280,'height':900});js=[]
 page.on('pageerror',lambda e:js.append(str(e)))
 while True:
  candidates=[x.parent for x in ROOT.rglob('VERIFICACION.json')]
  pilot=ROOT/'Negocios_Electronicos'/'Tema_1_1_Las_paginas_de_inicio'
  if pilot.exists():candidates.append(pilot)
  for folder in sorted(candidates):
   if (folder/'VERIFICACION_NAVEGADOR.json').exists() or (folder/'ERROR_NAVEGADOR.json').exists():continue
   try:
    start_errors=len(js);url=base+str(folder.relative_to(ROOT))+'/Actividad_Interactiva.html';page.goto(url)
    quiz=page.evaluate('preguntas');n=len(quiz);assert n in [8,10]
    for q in quiz:
     assert page.locator('#opciones button').count()==4
     page.locator('#opciones button').nth(q['answer']).click()
     assert page.locator('#respuesta').inner_text().startswith('Correcto.')
     assert all(b.is_disabled() for b in page.locator('#opciones button').all())
     page.locator('#siguiente').click()
    assert page.locator('#pregunta').inner_text()==f'Resultado: {n} de {n}'
    page.locator('#reiniciar').click()
    for q in quiz:
     page.locator('#opciones button').nth((q['answer']+1)%4).click()
     assert page.locator('#respuesta').inner_text().startswith('Revisa la respuesta.')
     page.locator('#siguiente').click()
    assert page.locator('#pregunta').inner_text()==f'Resultado: 0 de {n}'
    page.locator('#reiniciar').click();page.set_viewport_size({'width':390,'height':844})
    assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
    page.keyboard.press('Tab');page.keyboard.press('Enter');assert page.locator('#siguiente').is_visible()
    page.set_viewport_size({'width':1280,'height':900})
    playback={}
    for name,tag in [('Video.mp4','video'),('Audio.mp3','audio')]:
     result=page.evaluate('''async ({name,tag})=>{
       const m=document.createElement(tag);m.preload='auto';m.src=name;m.controls=true;document.body.replaceChildren(m);
       await new Promise((ok,fail)=>{m.onloadedmetadata=ok;m.onerror=()=>fail(Error('metadatos'));setTimeout(()=>fail(Error('tiempo agotado')),15000)});
       await m.play();await new Promise(ok=>setTimeout(ok,650));
       const r={duration:m.duration,currentTime:m.currentTime,paused:m.paused,error:m.error?.code||null,width:m.videoWidth||null,height:m.videoHeight||null};m.pause();m.removeAttribute('src');m.load();return r;
      }''',{'name':name,'tag':tag})
     assert result['currentTime']>.15 and not result['paused'] and result['error'] is None,result
     if tag=='video':assert result['width']==1920 and result['height']==1080
     playback[name]=result
    assert len(js)==start_errors,js[start_errors:]
    record=dict(questions=n,all_correct=f'{n}/{n}',all_incorrect=f'0/{n}',restart=True,keyboard=True,mobile_horizontal_overflow=False,javascript_errors=[],playback=playback)
    (folder/'VERIFICACION_NAVEGADOR.json').write_text(json.dumps(record,ensure_ascii=False,indent=2))
    print('NAVEGADOR OK '+folder.name,flush=True)
   except Exception as e:
    err=dict(folder=str(folder),error=str(e));errors.append(err);(folder/'ERROR_NAVEGADOR.json').write_text(json.dumps(err,ensure_ascii=False));print('ERROR NAVEGADOR '+str(err),flush=True)
  completed=len(list(ROOT.rglob('VERIFICACION_NAVEGADOR.json')))
  (BASE/'estado_navegador.json').write_text(json.dumps(dict(completed=completed,errors=errors),ensure_ascii=False,indent=2))
  if completed+len(errors)==27:break
  if (BASE/'estado.json').exists():
   st=json.loads((BASE/'estado.json').read_text())
   if st['pending']==0 and st['failed']:break
  time.sleep(5)
 browser.close()
server.shutdown();server.server_close()
