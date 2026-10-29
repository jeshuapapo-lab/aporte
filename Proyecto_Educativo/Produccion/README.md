# Regeneración de los materiales

Estos scripts generaron los archivos reales entregados. Requieren Python 3.12, FFmpeg con libx264/libmp3lame/AAC/libass, fuentes Noto Sans y, para las comprobaciones indicadas, Chromium y LibreOffice. Los nombres y rutas de binarios pueden requerir adaptación en otro sistema operativo. No hay llamadas a un servicio de voz remoto: la síntesis funciona localmente una vez descargado el modelo.

1. Crea un entorno virtual e instala `requirements.txt` con pip, conservando TLS y las verificaciones del gestor de paquetes. FFmpeg, Noto Sans, Chromium y LibreOffice son dependencias del sistema, no se distribuyen en el ZIP.
2. Descarga por HTTPS, desde las publicaciones oficiales, `kokoro-v1.0.onnx` y `voices-v1.0.bin`:
   - https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.1/kokoro-v1.0.onnx
   - https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.1/voices-v1.0.bin
   El origen oficial documenta el modelo como Apache 2.0 y el adaptador kokoro-onnx como MIT: https://github.com/thewh1teagle/kokoro-onnx . Los modelos no se redistribuyen en este proyecto.
3. Define `EDU_MODEL_DIR` con la carpeta de esos dos archivos. Para no sobrescribir los entregables o tus ediciones, define `EDU_PROJECT_DIR` con una **carpeta nueva** de salida y `EDU_BUILD_DIR` con una carpeta nueva de trabajo. `EDU_SOURCES_DIR` debe señalar a la carpeta Fuentes de esta entrega. Conserva el proxy y las autoridades de confianza de tu entorno.
4. Ejecuta, en este orden, con el Python del entorno virtual:
   ```sh
   python generar_documentos.py
   python generar_audio.py
   python montar_media.py
   ```
   Los dos primeros scripts escriben documentos, gráficos, guiones y narraciones; el tercero compone música original, normaliza la voz, crea escenas, añade subtítulos y monta el MP4 y el MP3 final. La velocidad efectiva empleada en esta entrega fue 1.0 y la fonetización, es-419. El adaptador de sesión corrige el tipo de entrada `speed` según el esquema float del modelo; no desactiva verificaciones.
5. Opcionalmente ejecuta `validar_interactivo.py` y `validar_multimedia.py` para pruebas reales de navegador. Usan un servidor temporal en loopback y lo detienen al terminar. La ruta del navegador usada en este entorno es `/usr/bin/chromium`.
6. La conversión de vista previa se hizo con LibreOffice, por ejemplo `soffice --headless --convert-to pdf --outdir CARPETA_PDF ARCHIVO.pptx`. Las vistas PDF deben regenerarse tras cambiar los editables.

`empaquetar.py` es el registro específico del empaquetado de esta entrega: espera los PDF convertidos en `EDU_BUILD_DIR/pdf`, fotogramas y el informe acústico de validación. No sustituye los pasos de generación, conversión y prueba. No edites `Validacion.md` para afirmar resultados de una regeneración sin volver a ejecutar las comprobaciones.

La generación reutiliza WAV existentes en su carpeta de trabajo. Si modificas los guiones, usa una carpeta `EDU_BUILD_DIR` nueva o elimina únicamente los WAV/JSON de producción que deban regenerarse; de lo contrario podría reutilizarse narración anterior. No se alteran los sílabos ni el repositorio aporte.
