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

Los JSON registran las comprobaciones reales. Educaplay remoto sigue sin verificarse por
restricción de red; la igualdad de enlaces con el reparto del usuario es una comprobación
diferente de la publicación y contenido de los juegos. Los índices declaran esa limitación.

El manifiesto usa rutas relativas a Proyecto_Educativo. Los archivos técnicos de esta
carpeta no se incluyen en el ZIP para el profesor, que contiene 44 archivos organizados.
