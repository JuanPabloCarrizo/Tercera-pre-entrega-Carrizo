from django.urls import path
from GaleriaApp import views

urlpatterns = [
    
    path('',views.inicio, name="Inicio"),
    path('artistas/',views.artistas, name="Artistas"),
    path('obras/',views.obras,name="Obras"),
    path('galerias/',views.galerias, name="Galerias"),
    path('api-artista-formulario/',views.api_artista_formulario, name="Api-Artista-Formulario"),
    path('api-obra-formulario/',views.api_obra_formulario, name="Api-Obra-Formulario"),    
    path('api-galeria-formulario/',views.api_galeria_formulario, name="Api-Galeria-Formulario"),
    path('api-busqueda-formulario/',views.api_busqueda_formulario, name="Api-Busqueda-Formulario"),
    
    # DEJO COMENTADO ESTO, PARA VER SI ME AYUDAN A RESOLVER ESTE DILEMA, QUIERO USAR EL MISMO FORMULARIO PARA MIS TRES MODELOS
    # PERO NO PUDE HACER QUE FUNCIONE SIMULTANEAMENTE LA BUSQUEDA
    # ASI Q SOLO DEJO LA DE BUSQUEDA DE ARTISTA, ESTO ES LO QUE HABÍA HECHO:
    # path('api-buscar-obra-formulario/', views.api_buscar_obra_formulario, name="Api-Buscar-Obra-Formulario"),
    # path('api-buscar-galeria-formulario/', views.api_buscar_galeria_formulario, name="Api-Buscar-Galeria-Formulario"),
       
    
]

# ¡CONSULTA!
    # EN EL PATH, EL PRIMER ATRIBUTO LO ESTABA PONIENDO SIN LA / AL FINAL.
    # IGUAL ME FUNCIONÓ BIEN.
    # ¿ES NECESARIA? EJEMPLO: ARTISTA VS ARTISTA/
    # path('artistas',views.artistas, name="Artistas"),
    # path('artistas/',views.artistas, name="Artistas"),
    # ¡GRACIAS!