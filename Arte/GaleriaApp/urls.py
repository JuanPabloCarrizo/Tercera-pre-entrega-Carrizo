from django.urls import path
from GaleriaApp import views
from django.views.generic import View


urlpatterns = [
    
    path('',views.inicio, name="Inicio"),
    path('artistas/', views.Artistas.as_view(),name="Artistas"),
    path('obras/', views.Obras.as_view(),name="Obras"),
    path('galerias/', views.Galerias.as_view(),name="Galerias"),
    path('artistas-panel/', views.ArtistasPanel.as_view(),name="Artistas-Panel"),
    path('artista-nuevo/',views.ArtistaCreate.as_view(),name="Artista-Nuevo"),
    path(r'^(?P<pk>\d+)$', views.ArtistaDetalle.as_view(),name="Artista-Detalle"),
    path(r'^editar/(?P<pk>\d+)$',views.ArtistaEditar.as_view(), name="Artista-Editar"),
    path('artista-eliminar/<int:pk>',views.ArtistaEliminar.as_view(),name="Artista-Eliminar"),
    path('obras-panel/', views.ObrasPanel.as_view(),name="Obras-Panel"),
    path('obra-nuevo/',views.ObraCreate.as_view(),name="Obra-Nuevo"),
    # path(r'^(?P<pk>\d+)$', views.ObraDetalle.as_view(),name="Obra-Detalle"),
    # path(r'^editar/(?P<pk>\d+)$',views.ObraEditar.as_view(), name="Obra-Editar"),
    # path('obra-eliminar/<int:pk>',views.ObraEliminar.as_view(),name="Obra-Eliminar"),
    
    path('galerias-panel/', views.GaleriasPanel.as_view(),name="Galerias-Panel"),    
    path('galeria-nuevo/',views.GaleriaCreate.as_view(),name="Galeria-Nuevo"),
    # path(r'^(?P<pk>\d+)$', views.GaleriaDetalle.as_view(),name="Galeria-Detalle"),
    # path(r'^editar/(?P<pk>\d+)$',views.GaleriaEditar.as_view(), name="Galeria-Editar"),
    # path('galeria-eliminar/<int:pk>',views.GaleriaEliminar.as_view(),name="Galeria-Eliminar"),

    

    
]

