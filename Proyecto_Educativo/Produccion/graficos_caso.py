from pathlib import Path
import json,sys,os
os.environ.setdefault('MPLCONFIGDIR','/workspace/edu-full/matplotlib-cache')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
sys.path.insert(0,'/workspace/edu-full')
from producir import folder
p=folder(json.loads(Path('/workspace/edu-full/content/PND_4_4.json').read_text()))/'Recursos'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(1,3,figsize=(13.2,4.5),layout='constrained')
for ax,vals,title,unit,note in zip(axs,[[40,24],[12,5],[80,95]],['Ciclo promedio','Casos con corrección','Respuesta en ≤48 horas'],['Horas','Porcentaje','Porcentaje'],['40 % de reducción','−7 puntos porcentuales','+15 puntos porcentuales']):
 bars=ax.bar(['Inicial','Futuro simulado'],vals,color=['#18394A','#087E8B'],width=.6);ax.set_title(title,fontweight='bold');ax.set_ylabel(unit);ax.set_ylim(0,max(vals)*1.25);ax.bar_label(bars,labels=[str(x) for x in vals],padding=5,fontweight='bold');ax.text(.5,-.19,note,transform=ax.transAxes,ha='center',color='#087E8B',fontweight='bold')
fig.suptitle('Estudio de caso BPM · 100 casos por período',fontsize=17,fontweight='bold')
fig.supxlabel('Datos sintéticos de enseñanza. Los resultados no demuestran un efecto causal en una empresa real.',fontsize=10)
for ext in ['png','svg']:fig.savefig(p/f'Comparacion_KPI.{ext}',dpi=180,bbox_inches='tight')
plt.close(fig)
fig,ax=plt.subplots(figsize=(10,4.6),layout='constrained');x=range(4)
a=ax.bar([i-.18 for i in x],[0,80,20,0],.36,label='Inicial',color='#18394A');b=ax.bar([i+.18 for i in x],[95,0,0,5],.36,label='Futuro simulado',color='#087E8B');ax.bar_label(a,padding=3);ax.bar_label(b,padding=3);ax.set_xticks(list(x),['20 h','30 h','80 h','100 h']);ax.set_ylabel('Casos (de 100)');ax.set_xlabel('Tiempo de ciclo');ax.set_ylim(0,110);ax.set_title('La mejora de la media conserva excepciones importantes',fontweight='bold');ax.legend();fig.supxlabel('Cinco casos futuros alcanzan cien horas. Datos simulados; revisar extremos además de promedios.',fontsize=10)
for ext in ['png','svg']:fig.savefig(p/f'Distribucion_tiempos.{ext}',dpi=180,bbox_inches='tight')
print('Gráficos de KPI y distribución generados.')
