import json
import functools, http.server, threading
from pathlib import Path
from playwright.sync_api import sync_playwright
from contenido import TOPIC, QUIZ

handler=functools.partial(http.server.SimpleHTTPRequestHandler,directory=str(TOPIC))
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),handler)
threading.Thread(target=server.serve_forever,daemon=True).start()

with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True)
    page=browser.new_page(viewport={'width':1280,'height':900})
    errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
    page.goto(f'http://127.0.0.1:{server.server_port}/Actividad_Interactiva.html')
    assert page.title()=='Práctica · Las páginas de inicio'
    for i,q in enumerate(QUIZ):
        assert page.locator('#contador').inner_text()==f'Pregunta {i+1} de 10'
        assert page.locator('#pregunta').inner_text()==q['q']
        assert page.locator('#opciones button').count()==4
        page.locator('#opciones button').nth(q['answer']).click()
        assert page.locator('#respuesta').inner_text().startswith('Correcto.')
        assert all(b.is_disabled() for b in page.locator('#opciones button').all())
        page.locator('#siguiente').click()
    assert page.locator('#pregunta').inner_text()=='Resultado: 10 de 10'
    page.locator('#reiniciar').click()
    for q in QUIZ:
        page.locator('#opciones button').nth((q['answer']+1)%4).click()
        assert page.locator('#respuesta').inner_text().startswith('Revisa la respuesta.')
        page.locator('#siguiente').click()
    assert page.locator('#pregunta').inner_text()=='Resultado: 0 de 10'
    page.locator('#reiniciar').click()
    page.set_viewport_size({'width':390,'height':844})
    assert page.evaluate('document.documentElement.scrollWidth<=window.innerWidth')
    page.keyboard.press('Tab');page.keyboard.press('Enter')
    assert page.locator('#siguiente').is_visible()
    page.screenshot(path=str(TOPIC/'Recursos'/'Vista_actividad_movil.png'),full_page=True)
    assert not errors,errors
    browser.close()
server.shutdown();server.server_close()
print(json.dumps({'quiz_preguntas':10,'ruta_correcta':'10/10','ruta_incorrecta':'0/10','reinicio':True,'teclado':True,'movil_sin_desbordamiento':True,'errores_javascript':errors},ensure_ascii=False))
