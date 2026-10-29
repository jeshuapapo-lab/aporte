import functools, http.server, json, threading
from playwright.sync_api import sync_playwright
from contenido import TOPIC

handler=functools.partial(http.server.SimpleHTTPRequestHandler,directory=str(TOPIC))
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),handler)
threading.Thread(target=server.serve_forever,daemon=True).start()
results={}
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True)
    page=browser.new_page()
    page.goto(f'http://127.0.0.1:{server.server_port}/')
    for name,tag in [('Video.mp4','video'),('Audio.mp3','audio')]:
        result=page.evaluate('''async ({name,tag})=>{
          const m=document.createElement(tag);m.preload='auto';m.src=name;m.controls=true;document.body.replaceChildren(m);
          await new Promise((ok,fail)=>{m.onloadedmetadata=ok;m.onerror=()=>fail(new Error('Error de metadatos'));setTimeout(()=>fail(new Error('Tiempo agotado')),15000)});
          await m.play();await new Promise(ok=>setTimeout(ok,900));
          const r={duration:m.duration,currentTime:m.currentTime,paused:m.paused,error:m.error?.code||null,width:m.videoWidth||null,height:m.videoHeight||null};
          m.pause();return r;
        }''',{'name':name,'tag':tag})
        assert result['currentTime']>0.3 and not result['paused'] and result['error'] is None,result
        if tag=='video':assert (result['width'],result['height'])==(1920,1080)
        results[name]=result
    browser.close()
server.shutdown();server.server_close()
print(json.dumps(results,ensure_ascii=False))
