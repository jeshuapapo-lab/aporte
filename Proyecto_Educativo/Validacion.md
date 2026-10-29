# Informe de validación · piloto NE 1.1

Comprobaciones ejecutadas el 29 de octubre de 2026. No se atribuye validación a contenidos que no se han generado.

| Elemento | Resultado comprobado |
|---|---|
| PPTX | Integridad ZIP/XML sin errores; reabierto con python-pptx y abierto/exportado por LibreOffice; 10 diapositivas editables y notas de narración. |
| DOCX tarea | Reabierto con python-docx y abierto/exportado por LibreOffice; 4 páginas, 6 ejercicios y rúbrica propuesta que suma 20 puntos. |
| Matriz | 27 filas de subtemas en CSV, 2 páginas en Word exportado a PDF. Títulos revisados contra la página 1 de cada sílabo. |
| Video | H.264, yuv420p, 1920×1080, 24 fps y pista AAC 48 kHz; 218,125 segundos. Decodificado de principio a fin sin errores con FFmpeg y reproducido en Chromium con avance temporal. |
| Audio | MP3, 44,1 kHz mono; aproximadamente 197,2 segundos. Decodificado íntegramente sin errores con FFmpeg y reproducido en Chromium con avance temporal. |
| Práctica interactiva | 10 preguntas verificadas en Chromium. Todas correctas: 10/10; todas incorrectas: 0/10. Reinicio, retroalimentación y bloqueo de doble respuesta correctos. Uso de teclado y vista móvil 390×844 sin desbordamiento horizontal. Sin errores JavaScript. |
| Revisión visual | Diapositivas abiertas realmente con LibreOffice y exportadas a PDF; hoja de contacto revisada. Tarea revisada en PDF; se corrigió la paginación y los anchos de la rúbrica. Fotogramas extraídos del MP4 comprobado. |

## Sonoridad de los archivos finales

| Archivo | Sonoridad integrada LUFS | Pico verdadero dBTP |
|---|---:|---:|
| Video.mp4 | -17.45 | -1.84 |
| Audio.mp3 | -17.22 | -1.33 |

Medidas obtenidas con el analizador loudnorm de FFmpeg sobre los archivos finales. Pico verdadero inferior a 0 dBTP en ambos. La música original se generó a nivel reducido y se atenuó con sidechain durante la narración.

## Límites de la comprobación

- Reproducción y análisis técnicos no equivalen a escucha humana. La voz neuronal usa ef_dora y fonetización latinoamericana es-419; no se certifica naturalidad, pronunciación o preferencia subjetiva sin revisión auditiva humana.
- Los subtítulos SRT y los incrustados usan segmentación proporcional por frase; no se realizó alineación fonética forzada.
- Educaplay no se publicó ni se probó dentro de una cuenta. Se validó una práctica HTML independiente que usa el mismo banco y se dejaron instrucciones para publicar y revisar la versión del servicio.
- Las pruebas no abarcan todos los reproductores, todas las versiones de Office ni un cumplimiento completo de WCAG.
- Este informe corresponde al piloto entregado, no a los otros 26 subtemas ni a futuras regeneraciones.
- La integridad final del ZIP se verifica por CRC al empaquetar y los archivos internos están inventariados en MANIFIESTO_SHA256.txt.

Detalles de códecs, duraciones y resultados: Validacion.json. Scripts de pruebas reales: Produccion/validar_interactivo.py y Produccion/validar_multimedia.py.