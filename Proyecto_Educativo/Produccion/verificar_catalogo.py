import functools,http.server,threading,json
from pathlib import Path
from playwright.sync_api import sync_playwright
root=Path('/workspace/Proyecto_Educativo_Completo')
class Quiet(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
srv=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(root)));threading.Thread(target=srv.serve_forever,daemon=True).start()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True);page=b.new_page(viewport={'width':1440,'height':1100});errors=[];page.on('pageerror',lambda e:errors.append(str(e)));page.goto(f'http://127.0.0.1:{srv.server_port}/index.html')
 assert page.locator('article:visible').count()==27
 page.locator('[data-filter=NE]').click();assert page.locator('article:visible').count()==12
 page.locator('[data-filter=PND]').click();assert page.locator('article:visible').count()==15
 page.locator('[data-filter=all]').click()
 for q,n in [('CRM',1),('certificaciones',1),('paginas',2),('gestion',2),('3.4',2),('xxxyyyzz',0)]:
  page.locator('#buscar').fill(q);assert page.locator('article:visible').count()==n,(q,page.locator('article:visible').count())
 page.locator('#buscar').fill('');page.set_viewport_size({'width':390,'height':844});assert page.evaluate('document.documentElement.scrollWidth<=innerWidth');page.set_viewport_size({'width':1440,'height':1100})
 page.screenshot(path=str(root/'Vista_catalogo.png'),full_page=False)
 assert not errors,errors;b.close()
srv.shutdown();srv.server_close()
(root/'VERIFICACION_CATALOGO.json').write_text(json.dumps(dict(cards=27,NE=12,PND=15,search_accent_insensitive=True,mobile_horizontal_overflow=False,javascript_errors=errors),ensure_ascii=False,indent=2))
print('Catálogo: filtros 12/15, búsqueda con y sin acentos, vacío y móvil correctos.')
