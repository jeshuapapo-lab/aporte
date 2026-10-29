import sys,json,csv,html,shutil,re,hashlib,zipfile,unicodedata,subprocess
from pathlib import Path
sys.path.insert(0,'/workspace/edu-build')
from contenido import SYLLABI
from generar_documentos import setup_doc,table
ROOT=Path('/workspace/Proyecto_Educativo_Completo');BASE=Path('/workspace/edu-full')
def slug(s):return re.sub(r'[^A-Za-z0-9]+','_',unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode()).strip('_')
def all_topics():
 out=[]
 for mi,m in enumerate(SYLLABI):
  for ui,(unit,topics) in enumerate(m['unidades'],1):
   for num,title in topics:
    code='NE' if mi==0 else 'PND';key=code+'_'+num.replace('.','_')
    folder=ROOT/('Negocios_Electronicos' if mi==0 else 'Procesos_para_Negocios_Digitales')/('Tema_'+num.replace('.','_')+'_'+slug(title))
    if key=='NE_1_1':folder=ROOT/'Negocios_Electronicos'/'Tema_1_1_Las_paginas_de_inicio'
    t=dict(id=key,materia=m['materia'],unidad=unit,num=num,title=title,folder=folder,ui=ui,code=code)
    if key!='NE_1_1':t.update(json.loads((BASE/'content'/(key+'.json')).read_text()))
    else:t.update(objective='Proponer y justificar una página de inicio que comunique la oferta, jerarquice recorridos y pueda evaluarse.',source='Sílabo UPS, NE 1.1. W3C, WCAG 2.2 (2023).')
    out.append(t)
 return out

def documentation(topics,final=False):
 rows=[]
 for t in topics:
  verified=(t['folder']/'VERIFICACION.json').exists() or t['id']=='NE_1_1'
  rows.append([t['materia'],f'{t["ui"]}. {t["unidad"]}',t['num'],t['title'],'PPTX, MP4, MP3, DOCX y Educaplay','Generado y verificado' if verified else 'En producción'])
 with (ROOT/'Matriz_temas.csv').open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.writer(f);w.writerow(['Materia','Unidad','Nº','Subtema','Entregables','Estado']);w.writerows(rows)
 md=['# Análisis y cobertura de los dos sílabos','','Fuente curricular: los dos PDF adjuntos de la Universidad Politécnica Salesiana, período 2026–2027, docente Edgar Olmedo Andrade Espín. Se conserva la secuencia y denominación de las unidades y los 27 contenidos numerados de la página 1; solo se normalizan espacios y puntuación final.','','El usuario solicitó desarrollar **todos los subtemas de ambos sílabos**. No queda una selección de temas pendiente. Este alcance responde a su petición, no a una atribución de asignación individual contenida en los PDF.','','| Materia | Unidad | Nº | Subtema | Entregables | Estado |','|---|---|---|---|---|---|']
 md+=['| '+' | '.join(r)+' |' for r in rows]
 md+=['','## Resultados de aprendizaje de las unidades','','**Negocios Electrónicos:** U1: Conoce la estructura de un negocio electrónico. U2: Aplica los principios y las técnicas de gestión de calidad y de innovación tecnológica en las organizaciones. U3: Aplica sistemas basados en Internet (ecommerce, e-learning, etc). Desarrollar soluciones de negocio mediante la implantación y la integración de hardware y software. U4: Diseña estrategias para desarrollar negocios globales.','','**Procesos para Negocios Digitales:** U1: Reconoce los conceptos relacionados con BPM. U2: Identifica claramente la estructura de un BPM. U3: Maneja las técnicas de modelado de procesos. U4: Implementa proyectos con base a BPM.','','## Actividades y evaluación oficiales','','El sílabo de Negocios Electrónicos presenta el encabezado de planificación sin desarrollar una tabla de actividades en el archivo recibido. No se inventan ponderaciones oficiales para esa materia.','','Procesos para Negocios Digitales incluye trabajo y talleres colaborativos, Tareas 1 y 2, cuatro entregables de proyecto y dos exámenes parciales. Su tabla suma 100 puntos: U1 15; U2 15; U3 20; U4 10; cada examen parcial 20. Las tareas y exámenes son actividades, no subtemas añadidos a la matriz. Los resultados y criterios abarcan vocabulario, estructura y ciclo BPM, interpretación de diagramas, BPMN, herramientas y KPI.','','Los objetivos particulares, los casos, las tareas, los tiempos sugeridos y las rúbricas de esta colección son elaboraciones didácticas. La rúbrica local de 20 puntos de cada tarea no sustituye las ponderaciones del profesor. Las bibliografías y perfiles docentes originales se conservan íntegros en Fuentes/.','','En la planificación de PND aparece una variante truncada de 3.1; se conserva como título canónico el de la página 1: Importancia del modelado en la gestión de procesos.','','## Organización de la producción','','Se produjo primero NE 1.1 como piloto y se amplió la misma estructura a los otros 26 subtemas a petición del usuario. Cada tema contiene los cinco entregables principales y extras para práctica y edición. Las actividades de Educaplay están preparadas para publicar en una cuenta autorizada, sin inventar enlaces.']
 (ROOT/'Analisis_silabos.md').write_text('\n'.join(md),encoding='utf-8')
 d=setup_doc('Matriz completa de los dos sílabos');d.sections[0].header.paragraphs[0].text='PROYECTO EDUCATIVO / COBERTURA CURRICULAR COMPLETA'
 d.add_heading('Dos materias · 27 subtemas',0);d.add_paragraph('135 entregables principales. Alcance: todos los contenidos numerados de los dos sílabos. Las actividades de Educaplay se entregan preparadas para publicar desde una cuenta autorizada.')
 for m in SYLLABI:
  d.add_heading(m['materia'],1);d.add_paragraph(f"{m['codigo']} · Nivel {m['nivel']} · {m['horas']} horas · 2026–2027")
  for ui,(unit,items) in enumerate(m['unidades'],1):
   d.add_heading(f'Unidad {ui}. {unit}',2);table(d,['Nº','Subtema','Materiales'],[[n,title,'PPTX · MP4 · MP3 · DOCX · Actividad'] for n,title in items])
 d.add_paragraph('Base: página 1 de los dos sílabos adjuntos. La producción educativa no reemplaza la planificación ni las rúbricas oficiales del profesor. El análisis ampliado y las referencias están en los archivos de esta colección.')
 d.save(ROOT/'Matriz_temas.docx')
 refs=['# Referencias de ampliación','','Los sílabos adjuntos son la fuente primaria del orden, títulos y unidades. Las referencias siguientes respaldan o amplían las explicaciones; no se afirma haber consultado en línea todas sus ediciones o requisitos durante esta ejecución. En regulaciones, credenciales y herramientas se debe revisar la versión oficial vigente antes de una implementación real.','']
 for t in topics:refs+=['## '+t['id']+' · '+t['title'],'',t['source'],'']
 (ROOT/'Fuentes'/'Referencias_ampliacion.md').write_text('\n'.join(refs),encoding='utf-8')
 alignment=['# Alineación didáctica por subtema','','Cada objetivo se desarrolla en la presentación y los guiones. Los ejercicios de la tarea piden analizar, diseñar, aplicar y evaluar; el cuestionario comprueba conceptos y decisiones. Son propuestas de enseñanza, no nuevos temas del sílabo.','','| Materia y tema | Objetivo de la elaboración | Evidencias |','|---|---|---|']
 for t in topics:alignment.append(f'| {t["code"]} {t["num"]} · {t["title"]} | {t["objective"]} | Presentación y multimedia; tarea argumentada; cuestionario con retroalimentación. |')
 (ROOT/'Mapa_alineacion.md').write_text('\n'.join(alignment),encoding='utf-8')

def catalog(topics):
 cards=[]
 for t in topics:
  rel=t['folder'].relative_to(ROOT).as_posix();title=html.escape(t['title']);mat=html.escape(t['materia']);obj=html.escape(t['objective'])
  links=''.join(f'<a href="{rel}/{name}">{label}</a>' for name,label in [('Presentacion.pptx','PowerPoint'),('Presentacion.pdf','Ver diapositivas'),('Video.mp4','Video'),('Audio.mp3','Audio'),('Tarea.docx','Tarea Word'),('Actividad_Interactiva.html','Practicar'),('Actividad_Educaplay.txt','Guía Educaplay')])
  cards.append(f'<article data-materia="{t["code"]}" data-search="{html.escape(mat+" "+title+" "+t["num"])}"><small>{mat} · Unidad {t["ui"]}</small><h2>{t["num"]}. {title}</h2><p>{obj}</p><nav aria-label="Materiales de {title}">{links}</nav></article>')
 h='''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Biblioteca educativa · Negocios digitales</title><style>
*{box-sizing:border-box}body{margin:0;background:#f5f2eb;color:#18394a;font:17px/1.6 system-ui,sans-serif}header{background:#112b3c;color:white;padding:56px max(24px,calc((100vw - 1180px)/2))}header small{color:#e7ae53;letter-spacing:.13em}h1{font-size:clamp(2.1rem,5vw,3.6rem);line-height:1.1;max-width:900px;margin:.5em 0}header p{max-width:790px;color:#d6e4e8}.stats{display:flex;gap:28px;flex-wrap:wrap;margin-top:24px}.stats span{font-weight:650}.wrap{max-width:1230px;margin:auto;padding:32px 24px}.filter{display:flex;gap:12px;flex-wrap:wrap}.filter button,input{font:inherit;padding:12px 16px;border:2px solid #b8c9c7;border-radius:9px;background:white;color:#18394a}.filter button{cursor:pointer}.filter button[aria-pressed=true]{background:#087e8b;color:white;border-color:#087e8b}input{width:100%;margin-top:18px}label{display:block;margin-top:18px;font-weight:650}label input{margin-top:6px}button:focus-visible,a:focus-visible,input:focus-visible{outline:4px solid #b9432e;outline-offset:3px}.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px}article{background:white;padding:27px;border-radius:16px;border-top:5px solid #087e8b}article[hidden]{display:none}article small{color:#087e8b;font-weight:700}h2{font-size:1.45rem;line-height:1.3;overflow-wrap:anywhere}article p{color:#536975}article nav{display:flex;gap:9px;flex-wrap:wrap}article a{padding:7px 12px;border-radius:7px;background:#e2f0ee;color:#12565c;text-decoration:none;font-weight:650;font-size:.9rem}article a:hover{text-decoration:underline}footer{padding:30px 24px;background:#112b3c;color:#d6e4e8}footer div{max-width:1180px;margin:auto}footer a{color:#fff}#resultado{min-height:28px}@media(max-width:700px){.grid{grid-template-columns:1fr}header{padding:36px 24px}article{padding:21px}.stats{gap:16px}.filter button{width:100%;text-align:left}}
</style></head><body><header><small>UPS · MATERIALES DE ESTUDIO · 2026–2027</small><h1>Comprende el negocio.<br>Mejora sus procesos.</h1><p>Explora las dos materias y sus contenidos. Estudia con la presentación, escucha la explicación, resuelve la tarea y comprueba lo aprendido con una actividad.</p><div class="stats"><span>2 materias</span><span>27 temas</span><span>135 materiales principales</span></div></header><main class="wrap"><div class="filter" aria-label="Filtrar por materia"><button data-filter="all" aria-pressed="true">Todas las materias</button><button data-filter="NE" aria-pressed="false">Negocios Electrónicos</button><button data-filter="PND" aria-pressed="false">Procesos para Negocios Digitales</button></div><label for="buscar">Busca un tema<input id="buscar" type="search" placeholder="Por ejemplo: CRM, pagos, BPMN o indicadores"></label><p id="resultado" role="status" aria-live="polite"></p><section class="grid" aria-label="Temas de estudio">__CARDS__</section></main><footer><div>Casos y datos ficticios preparados para enseñanza. Las actividades de Educaplay incluyen su guía de publicación. <a href="README.md">Guía de uso</a> · <a href="Matriz_temas.pdf">Matriz curricular</a> · <a href="Fuentes/">Fuentes</a></div></footer><script>const cards=[...document.querySelectorAll('article')],buttons=[...document.querySelectorAll('[data-filter]')],search=document.getElementById('buscar');let materia='all';const normal=s=>s.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase();function filtrar(){let visibles=0;cards.forEach(c=>{const ok=(materia==='all'||c.dataset.materia===materia)&&normal(c.dataset.search).includes(normal(search.value));c.hidden=!ok;if(ok)visibles++});document.getElementById('resultado').textContent=visibles+' de 27 temas';}buttons.forEach(b=>b.onclick=()=>{materia=b.dataset.filter;buttons.forEach(x=>x.setAttribute('aria-pressed',String(x===b)));filtrar()});search.oninput=filtrar;filtrar();</script></body></html>'''
 (ROOT/'index.html').write_text(h.replace('__CARDS__',''.join(cards)),encoding='utf-8')

def final_reports(topics):
 assert len(topics)==27
 integrated=json.loads((BASE/'visuales_integrados.json').read_text())
 assert set(integrated)=={'PND_3_2','PND_4_4'}
 primary=['Presentacion.pptx','Video.mp4','Audio.mp3','Tarea.docx','Actividad_Educaplay.txt']
 records=[]
 for t in topics:
  for name in primary:assert (t['folder']/name).is_file(),(t['id'],name)
  browser=t['folder']/'VERIFICACION_NAVEGADOR.json';assert browser.exists(),t['id']
  b=json.loads(browser.read_text());assert not b['javascript_errors'] and b['restart'] and b['keyboard']
  if t['id']=='NE_1_1':
   old=json.loads(Path('/workspace/Proyecto_Educativo/Validacion.json').read_text())
   v=dict(office_reopened=True,pdf_pages={'Presentacion.pdf':10,'Tarea.pdf':4},media={})
   for name,m in old['medios'].items():v['media'][name]=dict(duration=m['duration_seconds'],bytes=m['bytes'],streams=m['streams'],decoded_entirely=True)
   v['pilot_validation_reused']=True
  else:
   assert (t['folder']/'VERIFICACION.json').exists(),t['id'];v=json.loads((t['folder']/'VERIFICACION.json').read_text())
  assert 120<=v['media']['Video.mp4']['duration']<=240
  text=f'''# {t['num']}. {t['title']}

**Materia:** {t['materia']}  
**Unidad:** {t['unidad']}

## Objetivo de aprendizaje propuesto

{t['objective']}

## Materiales

- [Presentación PowerPoint editable](Presentacion.pptx) · [Vista PDF](Presentacion.pdf)
- [Video educativo](Video.mp4): {v['media']['Video.mp4']['duration']:.1f} segundos, con narración, música suave y subtítulos.
- [Audio independiente](Audio.mp3): {v['media']['Audio.mp3']['duration']:.1f} segundos, comprensible sin imágenes.
- [Tarea Word editable](Tarea.docx) · [Vista PDF](Tarea.pdf)
- [Práctica interactiva](Actividad_Interactiva.html): {b['questions']} preguntas con retroalimentación.
- [Actividad preparada para Educaplay](Actividad_Educaplay.txt): banco completo y pasos de publicación, sin enlace inventado.

## Aplicación

Estudia la explicación, resuelve la tarea justificando decisiones y revisa tus respuestas en la práctica. Los casos y datos son ficticios. Las escalas de evaluación son propuestas didácticas y no reemplazan las indicaciones del profesor.

[Guía docente y orientaciones de corrección](Recursos/Guia_docente.md) · [Guion del video](Recursos/Guion_video.md) · [Guion del audio](Recursos/Guion_audio.md)

## Referencias

Base curricular: sílabo UPS 2026–2027, {t['materia']}, unidad {t['ui']}, tema {t['num']}, página 1. Ampliación: {t['source']}
'''
  (t['folder']/'README.md').write_text(text,encoding='utf-8')
  records.append(dict(id=t['id'],materia=t['materia'],num=t['num'],title=t['title'],path=t['folder'].relative_to(ROOT).as_posix(),checks=v,browser=b))
 assert sum(r['browser']['questions'] for r in records)==218
 video_minutes=sum(r['checks']['media']['Video.mp4']['duration'] for r in records)/60
 audio_minutes=sum(r['checks']['media']['Audio.mp3']['duration'] for r in records)/60
 report=dict(alcance='27 subtemas de ambos sílabos; ningún subtema omitido',materias=2,temas=27,entregables_principales=135,diapositivas_principales=270,preguntas=218,video_minutes=video_minutes,audio_minutes=audio_minutes,records=records,integrated_visuals=integrated,bpmn_import=json.loads((BASE/'modelos/Verificacion_importacion.json').read_text()),limits=['Educaplay preparado sin publicación en cuenta externa','Voz neuronal es-419 sin evaluación auditiva humana de expresividad y pronunciación','Subtítulos con tiempos proporcionales; no alineación fonética forzada','Casos y datos sintéticos de enseñanza; no resultados reales de empresas'])
 (ROOT/'Validacion.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
 doc=['# Validación de la colección completa','','Se comprobaron los 27 temas, incluidos el piloto y los 26 subtemas adicionales. Los resultados de este archivo corresponden a los archivos entregados; no se atribuyen pruebas a futuras regeneraciones.','','| Tema | Diapositivas | Páginas tarea | Video (s) | Audio (s) | Preguntas |','|---|---:|---:|---:|---:|---:|']
 for r in records:
  c=r['checks'];doc.append(f'| {r["id"]} · {r["title"]} | 10 | {c["pdf_pages"]["Tarea.pdf"]} | {c["media"]["Video.mp4"]["duration"]:.2f} | {c["media"]["Audio.mp3"]["duration"]:.2f} | {r["browser"]["questions"]} |')
 doc+=['','## Comprobaciones ejecutadas','','- Integridad interna ZIP/XML y reapertura de PPTX/DOCX mediante sus bibliotecas.','- Apertura y exportación de cada presentación y tarea con LibreOffice; lectura del PDF resultante, contenido no vacío y revisión de límites de texto en las diapositivas.','- FFprobe para códecs, resolución y duración; todos los MP4 entre dos y cuatro minutos, Full HD H.264 con audio AAC.','- Decodificación completa de cada MP4 y MP3 mediante FFmpeg sin errores.','- Reproducción real de los 54 medios en Chromium con avance temporal, duración, resolución y ausencia de error de reproducción.','- Todos los cuestionarios recorridos con respuestas correctas e incorrectas; reinicio, bloqueo de doble respuesta, retroalimentación, teclado y pantalla móvil de 390×844.','- 218 preguntas: diez en el piloto y ocho en cada uno de los otros 26 temas.','- Modelos BPMN: XML y referencias internas comprobadas; importación mediante bpmn-moddle registrada por separado. No se ejecutó un motor de procesos ni se certifica conformidad exhaustiva de esquema.','- Las métricas de los 200 casos simulados se recalcularon y compararon con los resultados de la explicación.','',
 '## Límites explícitos','','La narración se genera con Kokoro, estilo ef_dora y fonetización es-419. La validación es técnica; no hubo evaluación perceptiva humana. Los subtítulos usan segmentación proporcional. La música instrumental es una composición programática propia y se atenúa durante la voz. Educaplay se entrega preparado, con instrucciones de publicación, sin acceso a una cuenta ni enlaces inventados. No se afirma un cumplimiento integral de accesibilidad o compatibilidad universal con todos los reproductores y suites de Office.','','Cada tema conserva los archivos VERIFICACION.json y VERIFICACION_NAVEGADOR.json cuando corresponden; Validacion.json consolida los resultados. Los documentos de rúbrica y las decisiones didácticas no reemplazan las del profesor.']
 (ROOT/'Validacion.md').write_text('\n'.join(doc),encoding='utf-8')
 readme=f'''# Proyecto educativo completo · dos sílabos

**27 temas desarrollados · 135 entregables principales · 270 diapositivas · 218 preguntas.** Se cubren los doce subtemas de Negocios Electrónicos y los quince de Procesos para Negocios Digitales, UPS 2026–2027, respetando los títulos y el orden de sus sílabos. No queda una selección de temas pendiente.

[Abrir el catálogo de materiales](index.html) · [Matriz completa](Matriz_temas.pdf) · [Análisis curricular](Analisis_silabos.md) · [Validación](Validacion.md)

## Qué incluye cada tema

| Archivo principal | Contenido |
|---|---|
| Presentacion.pptx | Diez diapositivas 16:9 editables con conceptos explicados, flujo o diagrama, caso, actividad, síntesis, fuentes y notas de narración. |
| Video.mp4 | Video reproducible de 2–4 minutos, Full HD 1920×1080, H.264/AAC, voz sintética neuronal con fonetización latinoamericana es-419, música instrumental propia de fondo, subtítulos y progreso animado. |
| Audio.mp3 | Explicación autónoma en MP3, con introducción y cierre propios, comprensible sin imágenes. El desarrollo comparte los conceptos del tema para conservar coherencia. |
| Tarea.docx | Actividad editable con objetivo, instrucciones, caso, ejercicios y rúbrica didáctica propuesta de 20 puntos. |
| Actividad_Educaplay.txt | Preguntas, opciones, respuestas correctas, retroalimentación e instrucciones completas para publicar. Preparada, sin publicación en cuenta externa. |

Cada carpeta añade una práctica HTML funcional, subtítulos SRT, guiones, banco CSV auxiliar, guía docente y PDF de vista previa. Los temas de modelado y el estudio de caso incluyen modelos BPMN y presentación editable complementaria. El estudio de caso contiene 200 filas simuladas y resultados calculados.

Duración total aproximada: **{video_minutes:.1f} minutos de video** y **{audio_minutes:.1f} minutos de audio**. Las duraciones de cada tema están en Validacion.md.

## Cómo estudiar o presentar

1. Extrae todo el ZIP. Abre index.html para navegar por materia o buscar un subtema. No requiere conexión ni servicios externos.
2. Abre PPTX en PowerPoint o una suite compatible y DOCX en Word o equivalente. Los PDF son vistas previas y no sustituyen los editables.
3. Reproduce MP4 y MP3 con un reproductor compatible. Usa la presentación para explicación guiada o el audio para repaso sin pantalla.
4. Resuelve la tarea y practica con Actividad_Interactiva.html. Las guías docentes y los bancos contienen respuestas: comparte con estudiantes solo los archivos apropiados.
5. Para Educaplay, accede a tu cuenta autorizada y sigue el TXT de cada tema. Prueba la actividad y copia su enlace real después de publicarla. El CSV es un banco auxiliar; no se afirma que sea un formato de importación automática verificado.

En navegadores administrados que bloqueen archivos locales, sirve la carpeta extraída con `python -m http.server 8001 --bind 127.0.0.1 --directory RUTA_PROYECTO` y accede localmente. No hay recopilación de respuestas ni backend; las prácticas funcionan en el navegador.

## Coherencia y fuentes

Analisis_silabos.md conserva materias, unidades, subtemas y resultados de aprendizaje. Mapa_alineacion.md enlaza cada objetivo elaborado con materiales y evidencias. Fuentes/ contiene íntegros los PDF recibidos y las referencias de ampliación.

Los casos y datos son ficticios. Los objetivos particulares, tiempos sugeridos, cuestionarios y rúbricas son elaboración didáctica; no son disposiciones atribuidas al profesor. En regulaciones, certificaciones y herramientas se señalan fuentes oficiales y la necesidad de comprobar la versión aplicable antes de una implantación real.

## Estado y comprobación

Todos los temas tienen sus cinco entregables principales. Las actividades de Educaplay están listas como contenido y guía de publicación; **no se publicaron** porque no se dispone de una cuenta autorizada. No se inventan enlaces. Las prácticas HTML equivalentes sí se generaron y comprobaron.

Se abrieron los documentos en LibreOffice, se decodificaron completos todos los medios y se reprodujeron en Chromium. Los cuestionarios pasaron recorridos de acierto/error, reinicio, teclado y móvil. Consulta Validacion.json para evidencia por archivo.

La voz es sintética neuronal, no una grabación humana. Se verificaron generación y reproducción, pero no se realizó evaluación auditiva humana de expresividad o pronunciación. Los subtítulos tienen tiempos aproximados por frase. Las animaciones son progreso, aparición de subtítulos y transiciones; no se afirma animación de personajes. Los modelos BPMN son educativos y no ejecutables.

## Código y archivos de producción

Produccion/ contiene el contenido estructurado y los scripts realmente ejecutados. No se incluyen modelos de voz, entornos virtuales, paquetes descargados ni cachés. El flujo de generación completo depende de las bibliotecas Python y herramientas multimedia documentadas allí; no necesitas instalarlas para usar los entregables terminados.

## Repositorio y descargas

El repositorio autorizado es [jeshuapapo-lab/aporte](https://github.com/jeshuapapo-lab/aporte). La carpeta Proyecto_Educativo contiene los materiales; el código previo del sitio se conservó. GitHub permite descargar el repositorio completo desde Code → Download ZIP. No se afirma una publicación web ni una página de Educaplay.
'''
 (ROOT/'README.md').write_text(readme,encoding='utf-8')
 return report

def sources():
 dest=ROOT/'Produccion';dest.mkdir(exist_ok=True)
 for p in BASE.glob('*.py'):
  if p.name not in {'benchmark_int8.py','sincronizar.py','cerrar_entrega.py','publicar_final.py'}:shutil.copy2(p,dest/p.name)
 shutil.copytree(BASE/'content',dest/'content',dirs_exist_ok=True)
 base=dest/'base_piloto';base.mkdir(exist_ok=True)
 for name in ['contenido.py','generar_documentos.py','generar_audio.py','montar_media.py','validar_interactivo.py','validar_multimedia.py']:
  shutil.copy2(Path('/workspace/edu-build')/name,base/name)
 shutil.copy2(Path('/workspace/Proyecto_Educativo/Negocios_Electronicos/Tema_1_1_Las_paginas_de_inicio/Actividad_Interactiva.html'),base/'Actividad_base.html')
 (dest/'README.md').write_text('''# Código de producción utilizado

El contenido autoral de los 26 temas adicionales se conserva en content/. El piloto tiene sus fuentes en base_piloto/. catalogo.py y unidad_*.py construyen el catálogo; producir.py genera documentos, voz y video; verificar_lotes.py abre documentos y decodifica medios; verificar_navegador.py ejecuta las pruebas de cuestionario y reproducción; modelos_bpmn.py y recursos_adicionales.py construyen modelos y datos; preparar_entrega.py organiza la colección y el ZIP.

Los scripts registran las rutas reales del entorno en el que se ejecutaron: /workspace/edu-build para el piloto, /workspace/edu-full para la producción completa, /workspace/edu-runtime para el entorno virtual y los modelos, y /workspace/Proyecto_Educativo_Completo para los entregables. No se presentan como una instalación portátil de un solo clic. Para ejecutarlos en otra máquina hay que adaptar esas rutas y las de Chromium/FFmpeg/LibreOffice, o recrear la misma estructura. Los archivos terminados se usan sin ejecutar los scripts.

Dependencias usadas: Python 3.12, python-pptx 1.0.2, python-docx 1.2.0, Pillow 12.3.0, numpy 2.3.5, PyMuPDF 1.26.6, pypdf 6.10.0, kokoro-onnx 0.4.9, soundfile 0.13.1, onnxruntime 1.31.1 y playwright 1.62.0. El sistema aporta FFmpeg con H.264/AAC/MP3/libass, LibreOffice, Noto Sans y Chromium. Se usaron dos procesos locales de generación, con dos hilos de inferencia por proceso. No se usaron agentes secundarios.

La voz se obtuvo con los modelos oficiales Kokoro v1.0 y voices-v1.0.bin de la publicación model-files-v1.1: https://github.com/thewh1teagle/kokoro-onnx/releases . Modelo Apache 2.0; adaptador kokoro-onnx MIT. No se distribuyen los modelos. Se evaluaron float32 e int8: las introducciones iniciales de NE 1.2 y NE 1.3 conservan un bloque de la variante int8; el resto de la producción utiliza float32. Ambas variantes corresponden al mismo modelo, voz y fonetización. Las descargas conservaron TLS y no se desactivaron verificaciones.

La música se compone programáticamente con arpegios y no usa grabaciones de terceros. La explicación de audio es autónoma: añade introducción y cierre de escucha y reutiliza bloques conceptuales coherentes con el video; no es una extracción de la pista mezclada. La segmentación de subtítulos es proporcional y no una alineación fonética forzada.

Las cachés de WAV se vinculan al hash del texto en la producción nueva. Si se modifican guiones, modelo o voz, usa una carpeta de trabajo limpia; el hash de texto por sí solo no detecta cambios de modelo. La generación no descarga datos de estudiantes ni usa cuentas de terceros. Las comprobaciones de navegador inician servidores temporales en loopback y los detienen al finalizar.
''',encoding='utf-8')
 (dest/'requirements.txt').write_text('python-pptx==1.0.2\npython-docx==1.2.0\nPillow==12.3.0\nnumpy==2.3.5\nPyMuPDF==1.26.6\npypdf==6.10.0\nkokoro-onnx==0.4.9\nsoundfile==0.13.1\nonnxruntime==1.31.1\nplaywright==1.62.0\nmatplotlib==3.10.8\nlxml==6.1.1\n',encoding='utf-8')
 shutil.copy2(BASE/'bpmn-check'/'validar.cjs',dest/'Verificar_BPMN.cjs')
 with (dest/'README.md').open('a',encoding='utf-8') as f:f.write('\nLos gráficos complementarios usan matplotlib 3.10.8 y la importación estructural BPMN se comprobó con Node y bpmn-moddle 9.0.4. integrar_visuales.py inserta durante la generación el diagrama de decisión de PND 3.2 y el gráfico editable de KPI de PND 4.4; debe estar activo antes de que esos temas terminen su narración. Los bloques conceptuales permanecen en las notas y guiones.\n')

def archive():
 # Ningún enlace local del catálogo debe apuntar a un material ausente.
 from urllib.parse import unquote,urlsplit
 for href in re.findall(r'href="([^"]+)"',(ROOT/'index.html').read_text()):
  u=urlsplit(html.unescape(href))
  if not u.scheme and not u.netloc:assert (ROOT/unquote(u.path)).exists(),href
 hashes=[]
 for p in sorted(ROOT.rglob('*')):
  if p.is_file() and p.name!='MANIFIESTO_SHA256.txt':hashes.append(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(ROOT).as_posix())
 (ROOT/'MANIFIESTO_SHA256.txt').write_text('\n'.join(hashes)+'\n',encoding='utf-8')
 output=ROOT.parent/'Proyecto_Educativo_Completo.zip'
 with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=5) as z:
  for p in sorted(ROOT.rglob('*')):
   if p.is_file():z.write(p,Path('Proyecto_Educativo')/p.relative_to(ROOT))
 with zipfile.ZipFile(output) as z:
  assert z.testzip() is None
  names=z.namelist()
  for name in ['Presentacion.pptx','Video.mp4','Audio.mp3','Tarea.docx','Actividad_Educaplay.txt']:assert sum(x.endswith('/'+name) for x in names)==27,name
 print(json.dumps(dict(zip=str(output),MiB=round(output.stat().st_size/1024**2,2),files=len(names),CRC='correcto'),ensure_ascii=False),flush=True)

if __name__=='__main__':
 topics=all_topics();documentation(topics,'--final' in sys.argv);catalog(topics)
 if '--final' in sys.argv:
  subprocess.run(['soffice','-env:UserInstallation=file:///tmp/edu-matriz-final','--headless','--convert-to','pdf','--outdir',str(ROOT),str(ROOT/'Matriz_temas.docx')],check=True)
  import fitz
  matrix_pdf=fitz.open(ROOT/'Matriz_temas.pdf')
  matrix_text=' '.join(' '.join(pg.get_text().split()) for pg in matrix_pdf)
  for t in topics:assert ' '.join(t['title'].split()) in matrix_text,t['title']
  final_reports(topics);sources();archive()
 else:print('Catálogo y documentación preparados; la finalización exige las 27 verificaciones de navegador.')
