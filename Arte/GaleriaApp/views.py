from django.shortcuts import render, redirect
# from django.http import HttpResponse, request
from GaleriaApp.models import *
from GaleriaApp.forms import *
from Usuarios.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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
    'artista_form': 'GaleriaApp/artista_form.html',
    'obra_form': 'GaleriaApp/obra_form.html',
    'galeria_form': 'GaleriaApp/galeria_form.html',
    'artista_detalle' : 'GaleriaApp/artista_detalle.html',
    'artista_editar' : 'GaleriaApp/artista_editar.html',
    'artista_confirm': 'GaleriaApp/artista_confirm_delete.html',
    
    'galerias_panel': 'GaleriaApp/galerias_panel.html',
    
    'listarGaleria': 'GaleriaApp/galeria_listar.html',
    'api_artistaForm': 'GaleriaApp/api_artista_formulario.html',
    'api_obraForm': 'GaleriaApp/api_obra_formulario.html',
    'api_galeriaForm': 'GaleriaApp/api_galeria_formulario.html',
    'api_busquedaForm': 'GaleriaApp/api_busqueda_formulario.html',
    'resultadoBusqueda': 'GaleriaApp/resultadoBusqueda.html',
}

# Vistas de Panel de control (cuando el user está logueado)
# @method_decorator(login_required, name='dispatch')
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
    fields = ["nombre", "nacionalidad", "fechaNac","fechaFallecimiento","movimiento"]

class ObraCreate(LoginRequiredMixin,CreateView):

    model = Obra
    template_name = plantillas['obra_form']
    success_url = reverse_lazy("Obras-Panel")
    fields = ["nombre", "autor", "anio","ubicacion","material"]
    
class GaleriaCreate(LoginRequiredMixin,CreateView):

    model = Galeria
    template_name = plantillas['galeria_form']
    success_url = reverse_lazy("Galeria-Panel")
    fields = ["nombre", "ubicacion", "obras"]
    
class ArtistaEditar(LoginRequiredMixin,UpdateView):
    model  = Artista
    template_name = plantillas['artista_editar']
    success_url = reverse_lazy("Artistas-Panel")
    fields = ["nombre", "nacionalidad", "fechaNac","fechaFallecimiento","movimiento"]
   
class ArtistaEliminar(LoginRequiredMixin,DeleteView):
    model = Artista
    success_url = reverse_lazy("Artistas-Panel")
    template_name = plantillas['artista_confirm']



# Vistas generales
def inicio(request):
    return render(request, plantillas['inicio'])

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
     
class ArtistaDetalle(DetailView):
    model = Artista
    template_name = plantillas['artista_detalle']
    
    # esto es para mostrar comentarios
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['comentario_form'] = ComentarioForm()
    #     context['comentarios'] = Comentario.objects.filter(artista=self.object)
    #     return context

    


# def obras(request):
#     obras = Obra.objects.all().values()        
#     info = {"obras": obras}
    
#     return render(request,pag_obra,info)

# def galerias(request):
#     galerias = Galeria.objects.all().values()        
#     info = {"galerias": galerias}
    
#     return render(request,pag_galeria,info)

# def api_artista_formulario(request):
    
#     if request.method == 'POST':
#         miFormulario = ArtistaFormulario(request.POST)        
#         if miFormulario.is_valid():
            
#             informacion= miFormulario.cleaned_data       
#             artista = Artista(nombre=informacion['nombre'],
#                             nacionalidad=informacion['nacionalidad'],
#                             fechaNac=informacion['fechaNac'],
#                             fechaFallecimiento=informacion['fechaFallecimiento'],
#                             movimiento=informacion['movimiento'])
        
#             artista.save()
           
#             print("\n\n terminó de guardar \n\n")
#             #return redirect(request, pag_artista)
#             return render(request,pag_inicio)
#     else:
#         miFormulario = ArtistaFormulario()
        
#     return render(request,pag_api_artistaForm,{"miFormulario": miFormulario})

# def api_obra_formulario(request):
    
#     if request.method == 'POST':
        
#         miFormulario = ObraFormulario(request.POST)        
#         if miFormulario.is_valid():
        
#             informacion= miFormulario.cleaned_data            
#             obra = Obra(nombre=informacion['nombre'],
#                             autor=informacion['autor'],
#                             anio=informacion['anio'],
#                             ubicacion=informacion['ubicacion'],
#                             material=informacion['material'])
            
#             obra.save()
#             return render(request,pag_inicio)
#     else:
#         miFormulario = ObraFormulario()
        
#     return render(request, pag_api_obraForm, {"miFormulario": miFormulario})

# def api_galeria_formulario(request):
    
#     if request.method == 'POST':
        
#         miFormulario = GaleriaFormulario(request.POST)
        
#         if miFormulario.is_valid():
            
#             informacion= miFormulario.cleaned_data
            
#             galeria = Galeria(nombre=informacion['nombre'],
#                             ubicacion=informacion['ubicacion'],
#                             obras=informacion['obras'])
            
#             galeria.save()
#             return render(request,pag_inicio)
#     else:
#         miFormulario= GaleriaFormulario()
            
#     return render(request,pag_api_galeriaForm,{"miFormulario":miFormulario})

# def api_busqueda_formulario(request):
    
#         if request.method == 'POST':       
                                
#                 miFormulario = BuscarArtistaForm(request.POST)        
#                 if miFormulario.is_valid():                    
#                     informacion= miFormulario.cleaned_data                        
#                     artistas = Artista.objects.filter(nombre__icontains=informacion["nombre"])                    
#                     return render(request,pag_resultadoBusqueda,{"artistas":artistas})

#                 else:                    
#                     respuesta = "No enviaste datos."                    
#                     return(request, pag_resultadoBusqueda,{"respuesta":respuesta})                   
#         else:          
#                 miFormulario = BuscarArtistaForm()
    
#         return render(request,pag_api_busquedaForm,{"miFormulario":miFormulario})
    
# def api_buscar_obra_formulario(request):
    
#     if request.method == 'POST':       
                
#         miFormulario = BuscarObraForm(request.POST)        
        
#         if miFormulario.is_valid():            
#             informacion= miFormulario.cleaned_data                
#             obras = Obra.objects.filter(nombre__icontains=informacion["nombre"])                        
#             return render(request,pag_resultadoBusqueda,{"obras":obras})

#         else:            
#             respuesta = "No enviaste datos."            
#             return(request, pag_resultadoBusqueda,{"respuesta":respuesta})                   
#     else:                   
#             miFormulario = BuscarObraForm()
    
#     return render(request,pag_api_busquedaForm,{"miFormulario":miFormulario})
    
# def api_buscar_galeria_formulario(request):
    
#     if request.method == 'POST':        
                
#         miFormulario = BuscarGaleriaForm(request.POST)        
        
#         if miFormulario.is_valid():            
#             informacion= miFormulario.cleaned_data                
#             galerias = Galeria.objects.filter(nombre__icontains=informacion["nombre"])                        
#             return render(request,pag_resultadoBusqueda,{"galerias":galerias})

#         else:            
#             respuesta = "No enviaste datos."            
#             return(request, pag_resultadoBusqueda,{"respuesta":respuesta})                   
#     else:                   
#             miFormulario = BuscarGaleriaForm()
    
#     return render(request,pag_api_busquedaForm,{"miFormulario":miFormulario})
    
# def listarArtista(request):
    
#     artistas = Artista.objects.all()
#     contexto = {"artistas": artistas}
#     return render(request,plantillas['listarArtista'],contexto)

# def eliminarArtista(request, artista_id):
     
#      #esto lo borra
#      artista = Artista.objects.get(id=int(artista_id))
#      artista.delete()
     
#      #esto vuelve a cargar la lista actualizada
#     #  artistas = Artista.objects.all()
#     #  contexto = {"artistas": artistas}
     
#     #  return render(request,pag_leerArtista,contexto)
#      return listarArtista(request)
 
# def editarArtista(request, artista_id):
    
#     print("Entro al EDITAR")
#     artista = Artista.objects.get(id=int(artista_id))
#     if request.method == "POST":
#         miFormulario = ArtistaFormulario(request.POST)
#         print("Entro al POST")
#         if miFormulario.is_valid():
#            print("Entro al is valid")
#            informacion = miFormulario.cleaned_data         
           
#            artista.nombre = informacion["nombre"]
#            artista.nacionalidad = informacion["nacionalidad"]
#            artista.fechaNac = informacion["fechaNac"]
#            artista.fechaFallecimiento = informacion["fechaFallecimiento"]
#            artista.movimiento = informacion["movimiento"]
#            artista.save()
           
#            return render(request,pag_inicio)
#     else:
        
#         print("ESto es el ELSE de editar, GET")
#         miFormulario = ArtistaFormulario(initial={'nombre': artista.nombre,'nacionalidad':artista.nacionalidad,'fechaNac':artista.fechaNac , 'fechaFallecimiento':artista.fechaFallecimiento})
            
#         return render(request,pag_api_artistaForm,{"miFormulario":miFormulario})

