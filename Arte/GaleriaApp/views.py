from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
# from django.http import HttpResponse, request
from GaleriaApp.models import *
from GaleriaApp.forms import *
from Usuarios.models import Avatar
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


#para comentarios
# from .models import Artista, Comentario
# from .forms import ComentarioForm

# Diccionario con direcciones 
plantillas = {
    'inicio': 'GaleriaApp/inicio.html',
    'login' : 'GaleriaApp/login.html',
    'register' : 'GaleriaApp/register.html',
    'artistas': 'GaleriaApp/artistas.html',
    'obras': 'GaleriaApp/obras.html',
    'galerias': 'GaleriaApp/galerias.html',
    'artistas_panel': 'GaleriaApp/artistas_panel.html',
    'obras_panel': 'GaleriaApp/obras_panel.html',
    'galerias_panel': 'GaleriaApp/galerias_panel.html',
    'artista_form': 'GaleriaApp/artista_form.html',
    'obra_form': 'GaleriaApp/obra_form.html',
    'galeria_form': 'GaleriaApp/galeria_form.html',
    'artista_detalle' : 'GaleriaApp/artista_detalle.html',
    'artista_editar' : 'GaleriaApp/artista_editar.html',
    'artista_confirm': 'GaleriaApp/artista_confirm_delete.html',
    'obra_detalle' : 'GaleriaApp/obra_detalle.html',
    'obra_editar' : 'GaleriaApp/obra_editar.html',
    'obra_confirm': 'GaleriaApp/obra_confirm_delete.html',
    'galeria_detalle' : 'GaleriaApp/galeria_detalle.html',
    'galeria_editar' : 'GaleriaApp/galeria_editar.html',
    'galeria_confirm': 'GaleriaApp/galeria_confirm_delete.html',
    'about': 'GaleriaApp/about.html',
}



# Vistas generales
def inicio(request):
    
    return render(request, plantillas['inicio'])

def about(request):
    
    return render(request, plantillas['about'])

class Artistas(ListView):
    model =  Artista
    template_name = plantillas['artistas']
    
    # def get(self, request, *args, **kwargs):
    #     return super().get(request,*args,**kwargs)
    
class Obras(ListView):
    model =  Obra
    template_name = plantillas['obras']
    
class Galerias(ListView):
    model = Galeria
    template_name = plantillas['galerias']
    
    # def get_queryset(self):
    #     # Incluir obras relacionadas en el queryset
    #     return Galeria.objects.prefetch_related('obra_set')
     
# Vistas de Panel de control (cuando el user está logueado)
class ArtistasPanel(LoginRequiredMixin,ListView):
    model =  Artista
    template_name = plantillas['artistas_panel']    
 
class ObrasPanel(LoginRequiredMixin,ListView):
    model =  Obra
    template_name = plantillas['obras_panel']

class GaleriasPanel(LoginRequiredMixin,ListView):
    model =  Galeria
    template_name = plantillas['galerias_panel']

class ArtistaCreate(LoginRequiredMixin,CreateView):

    model = Artista
    template_name = plantillas['artista_form']
    success_url = reverse_lazy("Artistas-Panel")
    form_class = ArtistaFormulario

class ObraCreate(LoginRequiredMixin,CreateView):


    model = Obra
    template_name = plantillas['obra_form']
    success_url = reverse_lazy("Obras-Panel")
    fields = ["nombre","cita","anio","material","biografia", "foto","artista","galeria"]
    

class GaleriaCreate(LoginRequiredMixin,CreateView):

    model = Galeria
    template_name = plantillas['galeria_form']
    success_url = reverse_lazy("Galerias-Panel")
    fields = ["nombre","cita", "ubicacion", "biografia", "foto"]
    
class ArtistaEditar(LoginRequiredMixin,UpdateView):
    model  = Artista
    template_name = plantillas['artista_editar']
    success_url = reverse_lazy("Artistas-Panel")
    form_class = ArtistaFormulario

class ObraEditar(LoginRequiredMixin,UpdateView):
    model  = Obra
    template_name = plantillas['obra_editar']
    success_url = reverse_lazy("Obras-Panel")
    fields = ["nombre","cita","anio","material","biografia", "foto","artista","galeria"]

class GaleriaEditar(LoginRequiredMixin,UpdateView):
    model  = Galeria
    template_name = plantillas['galeria_editar']
    success_url = reverse_lazy("Galerias-Panel")
    fields = ["nombre","cita", "ubicacion", "biografia", "foto"]

class ArtistaDetalle(DetailView):
    model = Artista
    template_name = plantillas['artista_detalle']

    #esto es para mostrar comentarios
    def post(self, request, *args, **kwargs):
        # Guarda los comentarios en la base de datos
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user  # Asocia el comentario con el usuario logueado.
            
            artista_id = self.kwargs.get('pk')
            if artista_id:
                
                comentario.artista_id = artista_id
            
            # Esto es porque sino tira error la base de datos.
            # El usuario puede o no comentar.
            try:
                comentario.obra_id = self.kwargs['obra_id']
            except KeyError:
                pass

            try:
                comentario.galeria_id = self.kwargs['galeria_id']
            except KeyError:
                pass

            try:
                comentario.artista_id = self.kwargs['artista_id']
            except KeyError:
                pass

            comentario.save()
                       
            # tomo el id del artista y dirijo al usuario a la sección comentario
            # así no tiene que ir al top de la página y scrollear para verlo.
            artist_pk = self.get_object().pk
            return HttpResponseRedirect(reverse('Artista-Detalle', args=[artist_pk]) + '#seccion-comentarios')


    # Esto es para enviar los comentarios y las obras relacionadas con el artista que se está viendo.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentario_form'] = ComentarioForm()
        context['comentarios'] = Comentario.objects.filter(artista=self.object)
        context['obras_del_artista'] = self.object.obras.all()
        
        return context
   
class ObraDetalle(DetailView):
    model = Obra
    template_name = plantillas['obra_detalle']
    
    #esto es para mostrar comentarios
    def post(self, request, *args, **kwargs):
        # Guarda los comentarios en la base de datos
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user  # Asocia el comentario con el usuario logueado.
            
            obra_id = self.kwargs.get('pk')
            
            if obra_id:
                
                comentario.obra_id = obra_id
            
            # Esto es porque sino tira error la base de datos.
            # El usuario puede o no comentar.
            try:
                comentario.obra_id = self.kwargs['obra_id']
            except KeyError:
                pass

            try:
                comentario.galeria_id = self.kwargs['galeria_id']
            except KeyError:
                pass

            try:
                comentario.artista_id = self.kwargs['artista_id']
            except KeyError:
                pass

            comentario.save()

           
            # tomo el id de la obra y dirijo al usuario a la sección comentario
            # así no tiene que ir al top de la página y scrollear para verlo.
            obra_pk = self.get_object().pk
            return HttpResponseRedirect(reverse('Obra-Detalle', args=[obra_pk]) + '#seccion-comentarios')
        
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['comentario_form'] = ComentarioForm()
            context['comentarios'] = Comentario.objects.filter(obra=self.object)
            
            return context

class GaleriaDetalle(DetailView):
    model = Galeria
    template_name = plantillas['galeria_detalle']
    
    #esto es para mostrar comentarios
    def post(self, request, *args, **kwargs):
        # Guarda los comentarios en la base de datos
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user  # Asocia el comentario con el usuario logueado.
            
            galeria_id = self.kwargs.get('pk')
            
            if galeria_id:
                
                comentario.galeria_id = galeria_id
            # Esto es porque sino tira error la base de datos.
            # El usuario puede o no comentar.
            try:
                comentario.obra_id = self.kwargs['obra_id']
            except KeyError:
                pass

            try:
                comentario.galeria_id = self.kwargs['galeria_id']
            except KeyError:
                pass

            try:
                comentario.artista_id = self.kwargs['artista_id']
            except KeyError:
                pass

            comentario.save()
           
            # tomo el id de la galeria y dirijo al usuario a la sección comentario
            # así no tiene que ir al top de la página y scrollear para verlo.
            galeria_pk = self.get_object().pk
            return HttpResponseRedirect(reverse('Galeria-Detalle', args=[galeria_pk]) + '#seccion-comentarios')  
    
    # Esto es para mostrar comentarios y las obras que están en esa galeria.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentario_form'] = ComentarioForm()
        context['comentarios'] = Comentario.objects.filter(galeria=self.object)
        context['obras_en_galeria'] = self.object.obras.all()
        return context
    
class ArtistaEliminar(LoginRequiredMixin,DeleteView):
    model = Artista
    success_url = reverse_lazy("Artistas-Panel")
    template_name = plantillas['artista_confirm']
    
class ObraEliminar(LoginRequiredMixin,DeleteView):
    model = Obra
    success_url = reverse_lazy("Obras-Panel")
    template_name = plantillas['obra_confirm']
    
class GaleriaEliminar(LoginRequiredMixin,DeleteView):
    model = Galeria
    success_url = reverse_lazy("Galerias-Panel")
    template_name = plantillas['galeria_confirm']
