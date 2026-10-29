import json,sys
from pathlib import Path
sys.path.insert(0,'/workspace/edu-build')
from contenido import SYLLABI
OUT=Path('/workspace/edu-full/content')
NAMES={('NE' if i==0 else 'PND',n):(m['materia'],u,t) for i,m in enumerate(SYLLABI) for u,topics in m['unidades'] for n,t in topics}

def add(code,num,objective,sections,flow,flowtext,case,problem,solution,tasks,questions,summary,source):
    materia,unit,title=NAMES[code,num]
    obj=dict(id=code+'_'+num.replace('.','_'),code=code,num=num,materia=materia,unidad=unit,title=title,objective=objective,sections=sections,flow=flow,flowtext=flowtext,case=case,problem=problem,solution=solution,tasks=tasks,summary=summary,source=source)
    assert len(sections)==4 and len(flow)==4 and len(tasks)==4 and len(questions)==8
    obj['questions']=[dict(q=q,correct=a,distractors=d,feedback=f) for q,a,d,f in questions]
    assert all(len(q['distractors'])==3 for q in obj['questions'])
    (OUT/(obj['id']+'.json')).write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf-8')

if __name__=='__main__':
    for p in sorted(Path(__file__).parent.glob('unidad_*.py')):exec(compile(p.read_text(),str(p),'exec'),globals())
    count=len(list(OUT.glob('*.json')))
    assert count==26,count
    (Path(__file__).parent/'CATALOGO_COMPLETO').write_text('26 subtemas adicionales preparados; se conserva el piloto NE 1.1.\n')
    print('Temas preparados:',count)
