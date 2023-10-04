# Tercera-pre-entrega-Carrizo
Tercera pre entrega, juan pablo carrizo. Web sobre una galería de arte online.

# La web "Galería de arte online", permite buscar, mostrar y agregar artistas, obras y museos.
1 - http://127.0.0.1:8000/GaleriaApp
2 - Tomé de base, este template: https://startbootstrap.com/template/small-business
3 - En la página principal, vemos el contenido de inicio.html que hereda de padre.html como archivo base.
4 - En inicio.html podemos buscar artistas, obras y galerias que están guardadas en la base de datos.
5 - Cargué 3 artistas, 2 obras y 2 galerias
6 - Cada uno de ellos, tiene una imagen. No se como guardarlas en la base, entonces lo que hice fué algo que simule:
    Puse imagenes en static/assets/img con la nomenclatura A, O y G (artista, obra y galeria) y un número secuencial.
    Dentro del for del html de cada uno de ellos le agregué:
    "src= {% static 'GaleriaApp/assets/img/A' %} {{ forloop.counter }} . jpg" 
    (lo saqué de google)
    Para simular que ya estaban guardadas. Hay un máximo disponible de fotos y luego ya no mostrará imágenes.
7 - Para agregar, en la navbar podemos hacerlo.
8 - Hay un botón buscar en la pantalla principal, la búsqueda es para ARTISTAS. 
    Luego si pueden me explican como hacer para utilizar los mismos html y views para que pueda filtrar los 3 modelos.
    Está hecho el código hasta donde pude pensar, pero luego solo dejé para que pueda buscar ARTISTAS.
9 - Creo q nada mas.
10 - El user del admin es jpcarrizo - Coderhouse01
