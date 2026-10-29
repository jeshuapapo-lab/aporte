# Proyecto educativo · piloto y planificación

## Qué contiene esta entrega

Se analizaron los dos sílabos de la Universidad Politécnica Salesiana, período 2026–2027: **Negocios Electrónicos** (12 subtemas) y **Procesos para Negocios Digitales** (15 subtemas). La matriz conserva las cuatro unidades de cada materia y los 27 subtemas en el orden de sus documentos.

**Alcance desarrollado: un piloto propuesto, Negocios Electrónicos, unidad 1, tema 1.1: «Las páginas de inicio».** Los PDF no asignan temas a un estudiante concreto. Los otros 26 subtemas solo están planificados; no se presentan como producidos ni como asignados. Desarrollarlos todos supondría 135 entregables principales.

## Archivos del piloto

Carpeta: `Negocios_Electronicos/Tema_1_1_Las_paginas_de_inicio/`

| Archivo | Contenido y estado |
|---|---|
| Presentacion.pptx | 10 diapositivas 16:9 editables, con explicación, diagrama de página, caso, aplicación, conclusión y referencias. Incluye guion en las notas. Abierta con LibreOffice y reabierta con python-pptx. |
| Video.mp4 | 3:38,125 · Full HD 1920×1080 · 24 fps · H.264/AAC. Narración sintética neuronal en español con fonetización latinoamericana es-419, ilustraciones y diagramas originales, subtítulos incrustados, transiciones y barra animada. Música instrumental original de teclado, a bajo nivel y atenuada durante la voz. |
| Audio.mp3 | Aproximadamente 3:17 · MP3 mono 44,1 kHz. Explicación independiente con contexto y pregunta de reflexión; no requiere mirar la presentación. Voz neuronal es-419, sin música para favorecer la escucha. |
| Tarea.docx | 4 páginas editables: objetivo, caso, instrucciones, 6 ejercicios, espacio para boceto, comprobaciones y rúbrica propuesta de 20 puntos. |
| Actividad_Educaplay.txt | Cuestionario completo de 10 preguntas con 4 opciones, respuesta correcta, retroalimentación, instrucciones y pasos para publicar. **Preparado, no publicado. No hay enlace de una actividad alojada.** |

Extras: actividad HTML interactiva sin conexión, banco CSV auxiliar, subtítulos SRT, guiones, guía docente con orientaciones de corrección, fotogramas reales y versiones PDF de la presentación y la tarea.

## Cómo usar los archivos

1. Extrae todo el ZIP antes de abrirlo. No necesitas ejecutar código para usar los materiales.
2. Abre PPTX y DOCX en PowerPoint/Word o una suite compatible. Los PDF sirven de vista previa y no sustituyen los editables.
3. Reproduce MP4 y MP3 en un reproductor que admita H.264/AAC y MP3. Ambos se reprodujeron en Chromium y se decodificaron por completo con FFmpeg.
4. Para practicar, abre `Actividad_Interactiva.html` en un navegador. Si tu navegador administrado bloquea archivos locales, sirve únicamente la carpeta del tema con `python -m http.server 8001 --bind 127.0.0.1 --directory RUTA_DEL_TEMA` y accede localmente. Es una práctica independiente, no una actividad de Educaplay; no recopila ni transmite respuestas.
5. Para publicar en Educaplay usa tu cuenta autorizada y sigue `Actividad_Educaplay.txt`. Prueba el enlace real con permisos de estudiante antes de compartirlo. El CSV es auxiliar: no se afirma compatibilidad con una importación automática del servicio.
6. La guía docente y el banco contienen respuestas. Comparte con estudiantes solo los archivos que correspondan a tu modalidad de evaluación.

## Alineación didáctica del piloto

Base curricular: U1 «Estructura del negocio electrónico», resultado «Conoce la estructura de un negocio electrónico», subtema 1.1 «Las páginas de inicio», p. 1 del sílabo.

| Objetivo didáctico propuesto | Desarrollo | Evidencia |
|---|---|---|
| Identificar la función del inicio y sus elementos | Diapositivas 1–3 y explicación multimedia | Tarea 1 y 3; cuestionario 1–2 |
| Redactar una oferta y jerarquizar una acción y recorridos | Diapositivas 4–5 y caso Minga Cacao | Tarea 2–4; cuestionario 3–5 y 10 |
| Justificar comprobaciones de accesibilidad y una medida de resultado | Diapositivas 6–7 | Tarea 5–6; cuestionario 6–9 |
| Aplicar e integrar los criterios en un boceto argumentado | Diapositivas 8–10, conclusión y fuentes | Boceto, justificaciones y revisión con la rúbrica |

Accesibilidad y medición son criterios de desarrollo de este subtema, no nuevos temas atribuidos al sílabo. La rúbrica de 20 puntos, los tiempos de trabajo y la referencia de 8/10 del cuestionario son propuestas propias: no reemplazan disposiciones del profesor. El caso **Minga Cacao** y las cifras usadas son ficticios. No se afirman ventas, certificaciones o resultados reales.

## Planificación de las dos materias

- `Analisis_silabos.md`: tabla completa, resultados de aprendizaje, actividades oficiales, límites y selección pendiente.
- `Matriz_temas.docx`, `.pdf` y `.csv`: listado de todos los temas con los cinco materiales requeridos.
- `Fuentes/`: los dos sílabos PDF originales, incluyendo sus bibliografías y perfil docente. El audio adjuntado por el usuario no se utilizó como fuente curricular ni se incluye en este ZIP.
- `Procesos_para_Negocios_Digitales/SELECCION_PENDIENTE.md`: registra que esta materia está analizada y todavía no tiene subtemas desarrollados.

## Verificación y límites

Consulta `Validacion.md`, `Validacion.json` y `MANIFIESTO_SHA256.txt`. La validación incluye integridad de Office, conversión por LibreOffice, revisión visual de documentos, reproducción en navegador, decodificación integral de medios, códecs y duración, y pruebas de las diez respuestas correctas e incorrectas del interactivo, reinicio, teclado y pantalla de 390 px.

La voz se genera con Kokoro, estilo ef_dora y fonetización es-419. No es una grabación humana. Se comprobó la generación, señal y reproducción; **no se realizó una evaluación perceptiva humana de expresividad o pronunciación**. Revisa auditivamente el piloto antes de entregarlo al profesor. Los subtítulos se segmentaron proporcionalmente dentro de cada frase sintetizada: sus tiempos son orientativos, no una alineación fonética forzada. Las animaciones son transiciones, aparición de subtítulos y progreso; no animación de personajes.

No hubo acceso a una cuenta autorizada de Educaplay, por lo que se entrega la preparación y una práctica local comprobada. No se ha publicado una actividad ni se ha inventado un enlace. Tampoco se ha enviado o publicado este proyecto en GitHub. El checkout de aporte permanece sin cambios.

## Código de producción

`Produccion/` incluye los scripts ejecutados y dependencias para regenerar documentos y multimedia, junto con instrucciones técnicas. El ZIP contiene los archivos finales; **no** incluye el entorno virtual ni los 338 MB de modelo/voces. Su descarga solo es necesaria si deseas sintetizar de nuevo la narración.

## Qué falta para continuar

Confirmar materia y números de los subtemas asignados o seleccionados con autorización del profesor. Con esa información se puede ampliar la producción conservando la estructura y el nivel del piloto. Esta entrega corresponde al análisis y al primer tema de prueba; no es una producción de los 27 temas.
