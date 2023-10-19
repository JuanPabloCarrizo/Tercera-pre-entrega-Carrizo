from django.urls import path
from GaleriaApp import views

urlpatterns = [
    
    path('',views.inicio, name="Inicio"),
    path('page-not-found/', views.page_not_found, name='Page_not_found'),
    path('artistas/', views.Artistas.as_view(),name="Artistas"),
    path('obras/', views.Obras.as_view(),name="Obras"),
    path('galerias/', views.Galerias.as_view(),name="Galerias"),
    # Artistas
    path('artistas-panel/', views.ArtistasPanel.as_view(),name="Artistas-Panel"),
    path('artista-nuevo/',views.ArtistaCreate.as_view(),name="Artista-Nuevo"),
    path('artista/<int:pk>', views.ArtistaDetalle.as_view(),name="Artista-Detalle"),
    path('artista-detalle/<int:pk>',views.ArtistaEditar.as_view(), name="Artista-Editar"),
    path('artista-eliminar/<int:pk>',views.ArtistaEliminar.as_view(),name="Artista-Eliminar"),
    # Obras
    path('obras-panel/', views.ObrasPanel.as_view(),name="Obras-Panel"),
    path('obra-nuevo/',views.ObraCreate.as_view(),name="Obra-Nuevo"),
    path('obra-detalle/<int:pk>', views.ObraDetalle.as_view(),name="Obra-Detalle"),
    path('obra-editar/<int:pk>',views.ObraEditar.as_view(), name="Obra-Editar"),
    path('obra-eliminar/<int:pk>',views.ObraEliminar.as_view(),name="Obra-Eliminar"),   
    # Galeria 
    path('galerias-panel/', views.GaleriasPanel.as_view(),name="Galerias-Panel"),    
    path('galeria-nuevo/',views.GaleriaCreate.as_view(),name="Galeria-Nuevo"),
    path('galeria-detalle/<int:pk>', views.GaleriaDetalle.as_view(),name="Galeria-Detalle"),
    path('galeria-editar/<int:pk>',views.GaleriaEditar.as_view(), name="Galeria-Editar"),
    path('galeria-eliminar/<int:pk>',views.GaleriaEliminar.as_view(),name="Galeria-Eliminar"),    
    # About
    path('about/',views.about, name="About"),
    
]

