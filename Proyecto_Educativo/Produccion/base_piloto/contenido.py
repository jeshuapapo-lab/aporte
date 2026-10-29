from pathlib import Path
import os

DEFAULT_ROOT = Path(__file__).resolve().parent.parent if Path(__file__).resolve().parent.name == 'Produccion' else Path('/workspace/Proyecto_Educativo')
ROOT = Path(os.environ.get('EDU_PROJECT_DIR',str(DEFAULT_ROOT)))
TOPIC = ROOT / 'Negocios_Electronicos' / 'Tema_1_1_Las_paginas_de_inicio'
BUILD = Path(os.environ.get('EDU_BUILD_DIR',str(ROOT.parent / 'edu-build')))
MODEL_DIR = Path(os.environ.get('EDU_MODEL_DIR',str(ROOT.parent / 'edu-runtime' / 'models')))
TITLE = 'Las páginas de inicio'
SUBTITLE = 'Negocios Electrónicos · Unidad 1 · Tema 1.1'

SYLLABI = [
 {'materia':'Negocios Electrónicos','codigo':'E-CA-LND-202','nivel':4,'horas':120,'archivo':'silabo_asignatura_417986 (1) (1).pdf','unidades':[
 ('Estructura del negocio electrónico', [('1.1','Las páginas de inicio'),('1.2','División por departamentos y categorías'),('1.3','Páginas de ventas y servicios'),('1.4','Aspectos institucionales')]),
 ('Sistemas empresariales electrónicos integrales',[('2.1','Tecnología en la gestión de cadena de valor'),('2.2','Metodología CRM')]),
 ('Sistemas para Mypes y Pymes y valor financiero de los sistemas electrónicos',[('3.1','Diferentes sistemas para Mypes y Pymes'),('3.2','Rendimiento financiero de los negocios electrónicos'),('3.3','Integraciones rentables de software y hardware'),('3.4','Sistemas de pago y documentos electrónicos')]),
 ('Sistemas para negocios globales y negocios móviles',[('4.1','Internacionalización de los negocios electrónicos'),('4.2','Aplicaciones para negocios móviles')])]},
 {'materia':'Procesos para Negocios Digitales','codigo':'E-CA-LND-214','nivel':8,'horas':160,'archivo':'silabo_asignatura_418022.pdf','unidades':[
 ('Introducción del BPM',[('1.1','Generalidades del BPM'),('1.2','Beneficios del BPM en los negocios digitales'),('1.3','Certificaciones'),('1.4','Ciclo de vida general del BPM')]),
 ('Estructura del BPM',[('2.1','Componentes clave del BPM'),('2.2','Fases del ciclo de vida del BPM'),('2.3','Rol del BPM en la mejora continua')]),
 ('Técnicas de modelado de procesos',[('3.1','Importancia del modelado en la gestión de procesos'),('3.2','Buenas prácticas de modelado'),('3.3','Herramientas digitales para modelado de procesos'),('3.4','Análisis y diagnóstico de procesos existentes y rediseño de procesos')]),
 ('Implementación del BPM',[('4.1','Planificación de un proyecto BPM'),('4.2','Indicadores para evaluar la implementación'),('4.3','Evaluación y selección de procesos a mejorar'),('4.4','Estudio de caso')])]}
]

# Elaboración didáctica original dentro del subtema 1.1. No son nuevos apartados del sílabo.
SLIDES = [
 {'tag':'COMPRENDER · DISEÑAR · EVALUAR','title':'Las páginas\nde inicio','kind':'cover','lead':'La primera orientación de un negocio electrónico.','note':'Pregunta guía: ¿qué debe entender y poder hacer una persona al llegar?',
 'narration':'Imagina que entras a una tienda y nadie te explica qué vende ni por dónde empezar. En internet ocurre lo mismo. La página de inicio debe orientar. En este tema aprenderás a reconocer sus elementos, proponer una estructura clara y evaluar si ayuda a las personas a avanzar.'},
 {'tag':'01 / PROPÓSITO','title':'Una puerta de entrada,\nno todo el negocio','kind':'cards','cards':[
 ('Qué es','Es la página principal que presenta la oferta y organiza el acceso al contenido del sitio.'),
 ('Qué resuelve','Responde qué ofrece el negocio, a quién ayuda y cuál es el siguiente paso relevante.'),
 ('Qué no implica','Una visita no siempre empieza aquí: también puede llegar a un producto desde una búsqueda.')],
 'takeaway':'La página de inicio orienta; una landing page suele concentrarse en una campaña u objetivo específico.',
 'narration':'La página de inicio presenta la oferta y distribuye los recorridos del sitio. Debe responder tres preguntas: qué ofrece el negocio, para quién y qué puedo hacer ahora. No todas las visitas comienzan aquí. Una persona también puede llegar directamente a un producto desde un buscador. Por eso, el resto del sitio necesita orientación coherente.'},
 {'tag':'02 / ESTRUCTURA','title':'Una jerarquía que\nayuda a decidir','kind':'anatomy',
 'items': [('Encabezado','Identidad y navegación con etiquetas claras.'),('Bloque principal','Beneficio central, imagen pertinente y acción prioritaria.'),('Contenido de apoyo','Oferta destacada y señales de confianza verificables.'),('Pie de página','Contacto, ayuda y enlaces de información legal.')],
 'narration':'Una estructura útil comienza con identidad y navegación. El bloque principal comunica el beneficio y presenta una acción prioritaria. Después, el contenido de apoyo muestra la oferta y aporta señales de confianza verificables. El pie reúne contacto, ayuda e información legal. No es una plantilla obligatoria: el orden se adapta al propósito y a las necesidades del público.'},
 {'tag':'03 / MENSAJE Y ACCIÓN','title':'Decir algo concreto.\nOfrecer un paso claro.','kind':'comparison',
 'left':('Mensaje ambiguo','«Calidad y pasión para ti»\n\nBotón: «Haz clic aquí»\n\nNo aclara qué se vende ni qué ocurrirá después.'),
 'right':('Propuesta específica','«Chocolate de cacao ecuatoriano para regalar»\n\nBotón: «Explorar regalos»\n\nRelaciona una oferta con una intención concreta.'),
 'takeaway':'Ejemplo ficticio: Minga Cacao. Solo promete entregas o certificaciones si puedes demostrarlas.',
 'narration':'Pensemos en Minga Cacao, un negocio ficticio de Guayaquil. El mensaje calidad y pasión para ti no explica su oferta. Chocolate de cacao ecuatoriano para regalar resulta más concreto. Un botón que dice explorar regalos anticipa mejor el destino que haz clic aquí. Evita prometer entregas o certificaciones que el negocio no puede demostrar.'},
 {'tag':'04 / RECORRIDOS','title':'Diseñar desde\nla intención del visitante','kind':'journey',
 'steps':[('Descubrir','Entender la oferta'),('Explorar','Encontrar opciones'),('Decidir','Elegir el siguiente paso')],
 'cards':[('Persona que ya sabe qué busca','Necesita acceso fácil al catálogo o búsqueda, si la oferta lo justifica.'),('Persona que aún está comparando','Necesita contexto, beneficios y evidencia para ganar confianza.')],
 'takeaway':'Una acción principal visible puede convivir con rutas secundarias bien jerarquizadas.',
 'narration':'Diseña los recorridos según la intención. Quien ya sabe lo que busca necesita acceder fácilmente a las opciones. Quien está comparando necesita contexto y evidencia. Priorizar una acción no significa eliminar las demás. Significa ordenar su importancia para que la página no obligue a elegir entre demasiadas llamadas que compiten entre sí.'},
 {'tag':'05 / MÓVIL Y ACCESIBILIDAD','title':'La claridad debe\nfuncionar para más personas','kind':'checklist',
 'items':[('Lectura cómoda','Texto legible, contenido adaptable y contraste suficiente.'),('Uso con teclado','Recorrido lógico y foco visible en enlaces y botones.'),('Imágenes que aportan','Texto alternativo cuando la imagen transmite información.'),('Acciones reconocibles','Etiquetas descriptivas; controles fáciles de localizar y activar.')],
 'takeaway':'WCAG 2.2: contraste mínimo 4,5:1 para texto normal; 3:1 para texto grande, con las excepciones del criterio 1.4.3.',
 'narration':'Comprueba la página en una pantalla pequeña y con teclado. ¿Se lee sin esfuerzo? ¿Se distingue dónde está el foco? Las imágenes informativas necesitan texto alternativo útil. Como referencia, las pautas de accesibilidad web establecen contraste mínimo de cuatro coma cinco a uno para texto normal, con excepciones. La claridad visual debe acompañarse de una experiencia que distintas personas puedan utilizar.'},
 {'tag':'06 / EVALUACIÓN','title':'Medir una acción\ncon un propósito definido','kind':'metric',
 'formula':'50 ÷ 2.000 × 100 = 2,5 %',
 'definition':'Ejemplo hipotético: 50 de 2.000 sesiones que vieron el inicio completaron la acción definida durante el período observado.',
 'cards':[('Define antes de medir','Qué acción cuenta, qué período observas y qué conjunto de sesiones usarás.'),('Interpreta con cuidado','Las visitas por sí solas no prueban utilidad. Un clic tampoco equivale a una venta.')],
 'takeaway':'La proporción observada describe un resultado; por sí sola no demuestra qué cambio lo causó.',
 'narration':'Elige una acción vinculada al objetivo antes de medir. Si cincuenta de dos mil sesiones que vieron el inicio completan esa acción, la proporción es dos coma cinco por ciento. Los datos son hipotéticos. Define el período y el conjunto de sesiones. Un clic no equivale a una venta, y una mejora observada no demuestra por sí sola qué cambio la causó.'},
 {'tag':'07 / APLICACIÓN','title':'Tu reto: mejorar\nel inicio de Minga Cacao','kind':'challenge',
 'items':[('Diagnostica','La página solo dice «Bienvenidos», tiene seis botones iguales y no explica qué vende.'),('Rediseña','Escribe una propuesta concreta y dibuja la jerarquía para una pantalla móvil.'),('Justifica','Explica la acción prioritaria, dos mejoras de accesibilidad y una medida de resultado.')],
 'takeaway':'Caso ficticio. No necesitas programar: entrega un boceto comentado y argumentos verificables.',
 'narration':'Ahora aplica el criterio. El inicio ficticio de Minga Cacao dice bienvenidos, muestra seis botones iguales y no explica la oferta. Propón un mensaje concreto, dibuja una versión móvil y elige una acción principal. Justifica dos decisiones de accesibilidad y una medida de resultado. No necesitas programar: debes demostrar por qué tu propuesta orienta mejor.'},
 {'tag':'08 / CONCLUSIÓN','title':'Orientar. Priorizar.\nComprobar.','kind':'conclusion',
 'cards':[('Orientar','Explica la oferta y permite reconocer qué puede hacerse en el sitio.'),('Priorizar','Ordena mensajes y recorridos según la intención del público.'),('Comprobar','Revisa accesibilidad y observa una acción definida con datos bien delimitados.')],
 'takeaway':'Antes de publicar: pide a otra persona que identifique la oferta y el siguiente paso sin ayuda.',
 'narration':'Recuerda tres ideas: orientar, priorizar y comprobar. Una buena página de inicio explica la oferta, ordena los recorridos y se evalúa con criterios claros. Antes de publicarla, pide a otra persona que identifique qué ofrece el negocio y cuál sería su siguiente paso, sin recibir ayuda. Su respuesta te dará una primera pista para mejorar.'},
 {'tag':'FUENTES Y CONTINUIDAD','title':'De la explicación\na la práctica','kind':'sources',
 'items':[('Base curricular','UPS · Negocios Electrónicos · 2026–2027. Unidad 1, subtema 1.1: «Las páginas de inicio». Página 1 del sílabo adjunto.'),('Referencia de accesibilidad','W3C (2023). Web Content Accessibility Guidelines (WCAG) 2.2. Criterios 1.1.1, 1.4.3, 1.4.10 y 2.4.7.'),('Siguiente paso','Resuelve Tarea.docx y practica con el cuestionario de 10 preguntas. El caso y los datos del ejemplo son ficticios.')],
 'takeaway':'Referencia técnica: https://www.w3.org/TR/WCAG22/ · Material didáctico de elaboración original.',
 'narration':'El tema corresponde al subtema uno punto uno del sílabo de Negocios Electrónicos. La referencia técnica de accesibilidad es la versión dos punto dos de las pautas del consorcio web. Continúa con la tarea y el cuestionario de práctica. Los ejemplos, el caso del negocio y sus cifras se elaboraron con fines educativos.'}
]

AUDIO_PARAGRAPHS = [
 'Bienvenido a esta explicación sobre las páginas de inicio de un negocio electrónico. Imagina que visitas una tienda en línea porque buscas un regalo. En pocos momentos necesitas entender qué vende, si la oferta te sirve y por dónde continuar. La página de inicio organiza esa primera orientación, aunque también puedes llegar al sitio directamente desde una página de producto.',
 'Su función no es mostrar todo al mismo tiempo. Es presentar la propuesta del negocio y ayudarte a encontrar un recorrido relevante. Una página de inicio puede atender distintas intenciones. Una página de campaña, también llamada landing page, suele concentrarse en un objetivo específico. Las dos deben expresar con claridad qué ofrecen y qué puedes hacer después.',
 'Recorre mentalmente una estructura sencilla. Arriba encuentras la identidad del negocio y la navegación. Luego aparece un mensaje principal con una imagen pertinente y una acción prioritaria. Más abajo puedes revisar la oferta destacada y señales de confianza comprobables. Al final están el contacto, la ayuda y los enlaces de información legal. El orden puede cambiar según las necesidades del público.',
 'Considera el caso ficticio de Minga Cacao, en Guayaquil. Decir calidad y pasión para ti suena agradable, pero no explica la oferta. Decir chocolate de cacao ecuatoriano para regalar permite reconocer el producto y una intención. Un botón con la frase explorar regalos anticipa el destino de la acción. Las promesas de entrega y las certificaciones solo deben mostrarse si el negocio puede respaldarlas.',
 'Haz una pausa breve y piensa en una página que conozcas. ¿Puedes identificar su oferta sin que alguien te la explique? ¿Sus botones dicen qué pasará al activarlos? Si todo compite por tu atención, probablemente falta jerarquía. Una acción principal puede convivir con enlaces secundarios, siempre que sus diferencias sean claras.',
 'La orientación también depende de la accesibilidad. Comprueba que la página se adapte a una pantalla pequeña. Recorre los enlaces con el teclado y observa si el foco es visible. Usa etiquetas descriptivas y texto alternativo para imágenes informativas. Para el texto normal, las pautas web establecen un contraste mínimo de cuatro coma cinco a uno, con excepciones que conviene revisar en la referencia técnica.',
 'Finalmente, define cómo evaluarás el resultado. Supón, con datos hipotéticos, que dos mil sesiones vieron el inicio y cincuenta completaron una acción previamente definida. La proporción es dos coma cinco por ciento. Es necesario especificar el período y el conjunto de sesiones. Esa cifra no demuestra por sí sola que un diseño causó el resultado, y un clic no debe confundirse con una venta.',
 'Tu actividad consiste en mejorar una página que solo dice bienvenidos y muestra seis botones iguales. Escribe una propuesta concreta, dibuja un boceto móvil y justifica la acción principal. Añade dos mejoras de accesibilidad y una medida de resultado. Conserva estas tres ideas: orientar, priorizar y comprobar. No necesitas imágenes para recordarlas; necesitas aplicarlas a decisiones concretas.'
]

QUIZ = [
 {'q':'¿Cuál es la función principal de una página de inicio?','options':['Orientar sobre la oferta y facilitar recorridos relevantes','Mostrar todo el catálogo completo en la primera pantalla','Sustituir todas las páginas del sitio','Garantizar una compra en cada visita'],'answer':0,'feedback':'La página principal presenta la oferta y organiza accesos; no garantiza compras ni sustituye el resto del sitio.'},
 {'q':'¿Qué afirmación sobre la llegada al sitio es correcta?','options':['Todas las visitas comienzan en el inicio','Una búsqueda puede llevar directamente a un producto','Solo se puede entrar desde un anuncio','La página de inicio impide accesos directos'],'answer':1,'feedback':'El inicio es una puerta de entrada, pero productos y otras páginas también reciben visitas directas.'},
 {'q':'En el caso ficticio Minga Cacao, ¿qué mensaje explica mejor la oferta?','options':['Bienvenidos a nuestra web','La excelencia que mereces','Chocolate de cacao ecuatoriano para regalar','Tu mejor experiencia está aquí'],'answer':2,'feedback':'El mensaje específico identifica qué se ofrece y una intención del público, sin promesas no verificadas.'},
 {'q':'¿Qué texto anticipa mejor el destino de un botón que abre la selección de regalos?','options':['Haz clic aquí','Más','Continuar ahora','Explorar regalos'],'answer':3,'feedback':'Una etiqueta descriptiva ayuda a prever la acción antes de activarla.'},
 {'q':'¿Qué decisión mejora la jerarquía de una página con seis botones iguales?','options':['Destacar una acción prioritaria y ordenar las secundarias','Cambiar todos los botones al mismo color brillante','Eliminar toda navegación','Añadir seis botones nuevos'],'answer':0,'feedback':'Priorizar ordena la atención sin impedir que existan otros recorridos pertinentes.'},
 {'q':'¿Qué comprobación aporta evidencia sobre el acceso con teclado?','options':['Contar cuántos colores tiene el sitio','Recorrer los controles y comprobar orden y foco visible','Ampliar la foto principal','Medir solamente las visitas'],'answer':1,'feedback':'El orden de navegación y el foco visible permiten identificar y utilizar los controles sin ratón.'},
 {'q':'Según WCAG 2.2, ¿cuál es el contraste mínimo general del texto normal en el criterio 1.4.3, sujeto a sus excepciones?','options':['1:1','2:1','4,5:1','10:1 en todos los casos'],'answer':2,'feedback':'El umbral para texto normal es 4,5:1; para texto grande es 3:1. El criterio contiene excepciones.'},
 {'q':'Con 50 sesiones que completan la acción de 2.000 que vieron el inicio, ¿qué proporción resulta?','options':['25 %','40 %','0,25 %','2,5 %'],'answer':3,'feedback':'Se calcula 50 dividido para 2.000, multiplicado por 100. Son datos hipotéticos.'},
 {'q':'¿Qué conclusión es válida si aumentan los clics en un botón?','options':['Hay más clics observados; todavía hay que comprobar el resultado del negocio','Todas las personas compraron','El diseño es la única causa posible','La accesibilidad ya está garantizada'],'answer':0,'feedback':'Un clic es una acción intermedia. No demuestra una venta, una causa única ni accesibilidad.'},
 {'q':'¿Qué debe acompañar una promesa de entrega o certificación?','options':['Una animación llamativa','Evidencia verificable de que el negocio puede respaldarla','Un botón de color rojo','La frase calidad garantizada sin más información'],'answer':1,'feedback':'Las señales de confianza deben poder demostrarse y no basarse en afirmaciones engañosas.'}
]

SOURCES = [
 ('Universidad Politécnica Salesiana (2026). Sílabo de Negocios Electrónicos, E-CA-LND-202. Unidad 1, tema 1.1, p. 1.', 'PDF adjunto por el usuario.'),
 ('Universidad Politécnica Salesiana (2026). Sílabo de Procesos para Negocios Digitales, E-CA-LND-214. Estructura curricular, p. 1; actividades y evaluación, pp. 2–6.', 'PDF adjunto por el usuario.'),
 ('W3C (2023). Web Content Accessibility Guidelines (WCAG) 2.2.', 'https://www.w3.org/TR/WCAG22/'),
]
