# Producción y comprobación de la entrega por unidades

Los scripts se ejecutaron en el entorno de trabajo real. `construir.py` consolida las
presentaciones y medios originales y elabora los talleres y prácticas de cada unidad.
`verificar.py` comprueba contenido, documentos Office, decodificación completa y navegador.
`indice_y_zip.py` genera la navegación, comprueba cobertura y empaqueta la entrega.

Los scripts conservan rutas del entorno de producción; para reproducirlos se necesita
la colección original, sus archivos de contenido, las herramientas y bibliotecas indicadas
en los imports y adaptar las rutas. La colección original se conserva en el historial
del repositorio, commit 1d5132a326768194c529c0d3a3bba99e20ed96a7, y en el respaldo local.
No se afirma que ejecutar estos scripts en una máquina nueva funcione sin preparar esa base.

Los JSON registran las comprobaciones reales. El PDF de enlaces aportado por el usuario
registra comprobación pública de los 27 juegos el 30/10/2026; esa prueba remota no se repitió
desde este entorno. Aquí se cotejaron los destinos, títulos, numeración, slugs y preguntas
con el sílabo, y se comprobó la integración de los enlaces en los ocho HTML de unidad.
Integrar_enlaces_directos.py recupera los destinos desde las anotaciones PDF, incluyendo
el enlace de PND 3.4 que aparece partido en dos líneas en el texto visible.

El manifiesto usa rutas relativas a Proyecto_Educativo. Los archivos técnicos de esta
carpeta no se incluyen en el ZIP para el profesor, que contiene 45 archivos organizados.
