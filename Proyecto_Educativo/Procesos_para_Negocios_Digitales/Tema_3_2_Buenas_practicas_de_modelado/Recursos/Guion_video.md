# Guion del video

## Escena 1

Hoy estudiaremos buenas prácticas de modelado. El propósito es aplicar convenciones básicas de BPMN y revisar decisiones, paralelismo y comunicación sin errores de flujo. Este contenido forma parte de procesos para negocios digitales. Trabajaremos con conceptos y un caso ficticio para tomar decisiones justificadas.

## Escena 2

Antes de proponer una solución, considera esta pregunta: ¿Por qué puede bloquearse el modelo y qué tipo de pasarela corresponde a la decisión del caso? Al terminar deberás explicar tu decisión, indicar cómo la comprobarías y reconocer los límites de la evidencia utilizada.

## Escena 3

En BPMN los eventos se representan con círculos, las actividades con rectángulos de esquinas redondeadas y las pasarelas con rombos. El marcador y el tipo de elemento cambian su significado. Nombra actividades con verbo y objeto, como verificar solicitud. Un rótulo claro comunica trabajo; etiquetas como trámite o gestión resultan demasiado ambiguas para revisar el comportamiento del recorrido.

## Escena 4

Una pasarela exclusiva selecciona una ruta según condiciones; una paralela abre todas sus salidas y puede sincronizar ramas paralelas al reunirlas. No uses una unión paralela para esperar rutas alternativas de una exclusiva: podría esperar una rama que nunca se activó. Las condiciones deben ser comprensibles y contemplar el caso que no satisface las opciones principales.

## Escena 5

Una solicitud se recibe y se verifica. Si está completa, avanza a la preparación de respuesta; si faltan datos, se solicita subsanación y se vuelve a comprobar cuando llega información. Esta decisión es exclusiva, no paralela. El recorrido debe indicar condiciones y evitar que la reunión espere simultáneamente dos alternativas que no se ejecutan juntas.

## Escena 6

Caso ficticio: un equipo dibuja una decisión completa o incompleta como una apertura paralela y después espera ambas ramas. Las solicitudes correctas quedan detenidas porque nunca recorrieron pedir datos. La corrección requiere representar una elección exclusiva con condiciones y una ruta de subsanación coherente. La revisión debe recorrer tanto una solicitud completa como otra incompleta, incluyendo qué sucede si el cliente no responde.

## Escena 7

Un pool delimita un participante y los carriles pueden distribuir responsabilidades dentro de él. Los flujos de secuencia conectan elementos de un mismo pool; los flujos de mensaje representan comunicación entre participantes distintos. Cruzar pools con secuencia confunde esos significados. Los carriles expresan organización del trabajo, pero no sustituyen una definición clara de responsabilidades y reglas.

## Escena 8

Recorre casos normales, incompletos y excepcionales. Comprueba que cada recorrido pueda empezar, avanzar y terminar según sus reglas, sin tareas inaccesibles ni esperas imposibles. Revisa también cancelaciones y eventos pertinentes al nivel del modelo. Una validación sintáctica en una herramienta detecta algunos errores, pero no garantiza que el modelo describa el negocio correcto ni que todas las condiciones estén bien formuladas.

## Escena 9

Para aplicar lo aprendido, desarrolla la tarea editable. Modela recibir, verificar y decidir con símbolos y nombres apropiados. Después, representa la comunicación con un cliente como participante externo sin cruzar pools con secuencia. Justifica tus decisiones con los conceptos de esta explicación y comprueba tus respuestas en la actividad interactiva.

## Escena 10

Conserva estas ideas. Usa símbolos y nombres con significado. Distingue alternativas de paralelismo. Revisa límites, mensajes y comportamiento. El caso y sus datos son ficticios. Revisa las fuentes indicadas en los materiales y continúa con la práctica para transferir estos criterios a otra situación.