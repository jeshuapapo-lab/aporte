from pathlib import Path
import json,re,shutil,sys
from urllib.parse import urlparse
import fitz

WORK=Path('/workspace/reorganizacion-unidades')
OUT=Path('/workspace/Entrega')
SOURCE=Path('/workspace/attachments/83a182e3-fa78-4345-b4b5-628b03571244/Enlaces_directos_Educaplay.pdf')
sys.path.insert(0,str(WORK))
from construir import slug,make_quiz

units=json.loads((WORK/'catalogo.json').read_text())
expected={t['id']:t for u in units for t in u['topics']}
mapping={}
with fitz.open(SOURCE) as doc:
    for page_number,page in enumerate(doc,1):
        text=page.get_text()
        labels=re.findall(r'^Sección (\d+\.\d+) - (.+)$',text,flags=re.M)
        counts=[int(n) for n in re.findall(r'^(\d+) preguntas \|',text,flags=re.M)]
        urls=list(dict.fromkeys(link['uri'] for link in page.get_links() if link.get('uri')))
        assert len(urls)==len(labels)==len(counts),(page_number,len(urls),len(labels),len(counts))
        for url,(number,title),count in zip(urls,labels,counts):
            parsed=urlparse(url)
            assert parsed.scheme=='https' and parsed.hostname=='es.educaplay.com'
            match=re.fullmatch(r'/recursos-educativos/(\d+)-(ne|pnd)_(\d+)_(\d+)_(.+)\.html',parsed.path)
            assert match,url
            activity_id,code,unit,section,title_slug=match.groups()
            ident=code.upper()+'_'+unit+'_'+section
            assert ident in expected and ident not in mapping,ident
            t=expected[ident]
            assert number==t['num'] and title==t['title'],(ident,number,title)
            assert title_slug==slug(t['title']).lower(),(ident,title_slug)
            assert count==len(t['questions'])
            mapping[ident]=dict(url=url,activity_id=activity_id,section=number,title=title,questions=count,
                                source_pdf_page=page_number,documental_title_number_and_slug_match=True,
                                source_pdf_reports_public_http200=True,source_pdf_check_date='2026-10-30',
                                independent_remote_check_in_this_environment=False)
assert set(mapping)==set(expected) and len(mapping)==27
assert len({r['activity_id'] for r in mapping.values()})==27
assert len({r['url'] for r in mapping.values()})==27
for u in units:
    for t in u['topics']:
        t['activity_url']=mapping[t['id']]['url']
        t['activity_evidence']=mapping[t['id']]
    make_quiz(u)
(WORK/'catalogo.json').write_text(json.dumps(units,ensure_ascii=False,indent=2))
(WORK/'Enlaces_directos_verificados_documentalmente.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2))
shutil.copy2(SOURCE,OUT/'01_Enlaces_directos_Educaplay.pdf')

report_path=WORK/'Verificacion_navegador.json'
report=json.loads(report_path.read_text())
for r in report:
    r.pop('profile_links_match_received_assignment',None)
    r['direct_activity_links_match_uploaded_pdf_and_syllabus']=True
    r['source_pdf_reports_public_http200_checks']=True
    r['independent_remote_check_in_this_environment']=False
report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({'enlaces_directos':len(mapping),'materias':2,'unidades':8,'numeros_titulos_slugs_y_preguntas_coinciden':True,
                  'url_larga_recuperada_desde_hipervinculo_pdf':mapping['PND_3_4']['url'],
                  'comprobacion_remota': 'Aportada en PDF del usuario; no repetida desde este entorno.'},ensure_ascii=False,indent=2))
