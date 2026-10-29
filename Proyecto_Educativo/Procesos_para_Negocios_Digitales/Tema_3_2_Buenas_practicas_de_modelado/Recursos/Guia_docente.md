# Guía docente · Buenas prácticas de modelado

Objetivo: Aplicar convenciones básicas de BPMN y revisar decisiones, paralelismo y comunicación sin errores de flujo.

## Orientación del caso

Completa o incompleta son alternativas: usar una exclusiva. No sincronizar rutas alternativas mediante una unión paralela que espere ambas. Definir subsanación, vuelta a comprobación y tratamiento del caso sin respuesta según el alcance.

## Conceptos y evidencias

### Símbolos con significado
En BPMN los eventos se representan con círculos, las actividades con rectángulos de esquinas redondeadas y las pasarelas con rombos. El marcador y el tipo de elemento cambian su significado. Nombra actividades con verbo y objeto, como verificar solicitud. Un rótulo claro comunica trabajo; etiquetas como trámite o gestión resultan demasiado ambiguas para revisar el comportamiento del recorrido.

### Decisiones y paralelismo
Una pasarela exclusiva selecciona una ruta según condiciones; una paralela abre todas sus salidas y puede sincronizar ramas paralelas al reunirlas. No uses una unión paralela para esperar rutas alternativas de una exclusiva: podría esperar una rama que nunca se activó. Las condiciones deben ser comprensibles y contemplar el caso que no satisface las opciones principales.

### Participantes y comunicación
Un pool delimita un participante y los carriles pueden distribuir responsabilidades dentro de él. Los flujos de secuencia conectan elementos de un mismo pool; los flujos de mensaje representan comunicación entre participantes distintos. Cruzar pools con secuencia confunde esos significados. Los carriles expresan organización del trabajo, pero no sustituyen una definición clara de responsabilidades y reglas.

### Validar comportamiento
Recorre casos normales, incompletos y excepcionales. Comprueba que cada recorrido pueda empezar, avanzar y terminar según sus reglas, sin tareas inaccesibles ni esperas imposibles. Revisa también cancelaciones y eventos pertinentes al nivel del modelo. Una validación sintáctica en una herramienta detecta algunos errores, pero no garantiza que el modelo describa el negocio correcto ni que todas las condiciones estén bien formuladas.

## Corrección

Valorar los cuatro ejercicios con la rúbrica de Tarea.docx. Admitir soluciones alternativas justificadas y coherentes con las restricciones. No asignar puntaje completo a una lista sin explicación. El caso y los datos son ficticios; el criterio del profesor prevalece sobre esta propuesta. Las respuestas y la retroalimentación del cuestionario están en Actividad_Educaplay.txt.
