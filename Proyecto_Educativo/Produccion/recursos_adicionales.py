import sys,csv,json,datetime,shutil
from pathlib import Path
from producir import folder
BASE=Path('/workspace/edu-full')
for key in ['PND_3_1','PND_3_2','PND_3_3','PND_3_4','PND_4_4']:
 t=json.loads((BASE/'content'/(key+'.json')).read_text());dest=folder(t)/'Recursos'/'Modelos_BPMN';dest.mkdir(parents=True,exist_ok=True)
 for p in (BASE/'modelos').iterdir():shutil.copy2(p,dest/p.name)
t=json.loads((BASE/'content/PND_4_4.json').read_text());res=folder(t)/'Recursos';res.mkdir(parents=True,exist_ok=True)
rows=[]
for period in ['inicial','futuro_simulado']:
 for i in range(100):
  dur=(80 if i<20 else 30) if period=='inicial' else (100 if i<5 else 20)
  start=datetime.datetime(2026,10,1,8)+datetime.timedelta(hours=i,days=0 if period=='inicial' else 21)
  end=start+datetime.timedelta(hours=dur)
  rows.append(dict(caso=('A' if period=='inicial' else 'B')+f'{i+1:03d}',periodo=period,recepcion=start.isoformat(),respuesta_util=end.isoformat(),horas_ciclo=dur,horas_trabajo=4,horas_espera=dur-4,requiere_correccion=int(i<(12 if period=='inicial' else 5)),cumple_48_horas=int(dur<=48),origen='simulacion_educativa'))
with (res/'Casos_soporte_simulados.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
metrics={}
for p in ['inicial','futuro_simulado']:
 g=[r for r in rows if r['periodo']==p];metrics[p]=dict(casos=len(g),promedio_horas=sum(r['horas_ciclo'] for r in g)/len(g),correccion_porcentaje=sum(r['requiere_correccion'] for r in g),cumplimiento_48_horas_porcentaje=sum(r['cumple_48_horas'] for r in g),maximo_horas=max(r['horas_ciclo'] for r in g))
assert metrics['inicial']['promedio_horas']==40 and metrics['futuro_simulado']['promedio_horas']==24
assert metrics['inicial']['cumplimiento_48_horas_porcentaje']==80 and metrics['futuro_simulado']['cumplimiento_48_horas_porcentaje']==95
(res/'Resultados_simulacion.json').write_text(json.dumps(metrics,ensure_ascii=False,indent=2))
(res/'Datos_LEEME.md').write_text('''# Datos sintéticos de soporte

200 filas: cien casos completos del período inicial y cien del futuro simulado. Las fechas son valores ficticios expresados como hora local sin zona para este ejercicio y no corresponden a operaciones reales. El cálculo usa horas transcurridas continuas, no horas laborables. Los grupos se construyeron para practicar comparación; no justifican una conclusión causal sobre una empresa real.

- Inicial: 80 casos de 30 horas y 20 de 80; media 40. Corrección en 12 casos. Cumplimiento de 48 horas: 80 %.
- Futuro simulado: 95 casos de 20 horas y cinco de 100; media 24. Corrección en cinco casos. Cumplimiento: 95 %.
- Trabajo: cuatro horas por caso; espera: ciclo menos cuatro.
- Variación relativa de media: (40−24)/40 = 40 % de reducción.
- Corrección: 12 % a 5 %, siete puntos porcentuales menos.
- Cumplimiento: 80 % a 95 %, quince puntos porcentuales más.
- Las cinco excepciones de cien horas requieren análisis aunque mejore la media.

Cada indicador se calcula sobre los cien casos completos de su período. En una operación real deben definirse cohortes, casos abiertos y abandonados para evitar sesgos. La variable de corrección indica que el caso requirió corrección y no cuántas veces ocurrió.
''',encoding='utf-8')
print(json.dumps(metrics,ensure_ascii=False))
