from django.shortcuts import render
from django.http import HttpResponse, request
from GaleriaApp.models import *
from GaleriaApp.forms import *
# acá pongo las direcciones, porque no me gustan como quedan en el return.
pag_inicio = "GaleriaApp/inicio.html"
pag_artista = "GaleriaApp/artistas.html"
pag_obra = "GaleriaApp/obras.html"
pag_galeria = "GaleriaApp/galerias.html"
pag_api_artistaForm = "GaleriaApp/api_artista_formulario.html"
pag_api_obraForm = "GaleriaApp/api_obra_formulario.html"
pag_api_galeriaForm = "GaleriaApp/api_galeria_formulario.html"
pag_api_busquedaForm = "GaleriaApp/api_busqueda_formulario.html"
pag_resultadoBusqueda = "GaleriaApp/resultadoBusqueda.html"

# Create your views here.
def inicio(request):
#    return HttpResponse('inicio')
    return render(request, pag_inicio)

def artistas(request):    
    artistas = Artista.objects.all().values()        
    info = {"artistas": artistas}
    
    return render(request,pag_artista,info)

def obras(request):
    obras = Obra.objects.all().values()        
    info = {"obras": obras}
    
    return render(request,pag_obra,info)

def galerias(request):
    galerias = Galeria.objects.all().values()        
    info = {"galerias": galerias}
    
    return render(request,pag_galeria,info)

def api_artista_formulario(request):
    
    if request.method == 'POST':
        miFormulario = ArtistaFormulario(request.POST)        
        if miFormulario.is_valid():
            
            informacion= miFormulario.cleaned_data       
            artista = Artista(nombre=informacion['nombre'],
                            nacionalidad=informacion['nacionalidad'],
                            fechaNac=informacion['fechaNac'],
                            fechaFallecimiento=informacion['fechaFallecimiento'],
                            movimiento=informacion['movimiento'])
        
            artista.save()
            return render(request,pag_inicio)
    else:
        miFormulario = ArtistaFormulario()
        
    return render(request,pag_api_artistaForm,{"miFormulario": miFormulario})

def api_obra_formulario(request):
    
    if request.method == 'POST':
        
        miFormulario = ObraFormulario(request.POST)        
        if miFormulario.is_valid():
        
            informacion= miFormulario.cleaned_data            
            obra = Obra(nombre=informacion['nombre'],
                            autor=informacion['autor'],
                            anio=informacion['anio'],
                            ubicacion=informacion['ubicacion'],
                            material=informacion['material'])
            
            obra.save()
            return render(request,pag_inicio)
    else:
        miFormulario = ObraFormulario()
        
    return render(request, pag_api_obraForm, {"miFormulario": miFormulario})

def api_galeria_formulario(request):
    
    if request.method == 'POST':
        
        miFormulario = GaleriaFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            informacion= miFormulario.cleaned_data
            
            galeria = Galeria(nombre=informacion['nombre'],
                            ubicacion=informacion['ubicacion'],
                            obras=informacion['obras'])
            
            galeria.save()
            return render(request,pag_inicio)
    else:
        miFormulario= GaleriaFormulario()
            
    return render(request,pag_api_galeriaForm,{"miFormulario":miFormulario})

def api_busqueda_formulario(request):
    
        if request.method == 'POST':       
                                
                miFormulario = BuscarArtistaForm(request.POST)        
                if miFormulario.is_valid():                    
                    informacion= miFormulario.cleaned_data                        
                    artistas = Artista.objects.filter(nombre__icontains=informacion["nombre"])                    
                    return render(request,pag_resultadoBusqueda,{"artistas":artistas})

                else:                    
                    respuesta = "No enviaste datos."                    
                    return(request, pag_resultadoBusqueda,{"respuesta":respuesta})                   
        else:          
                miFormulario = BuscarArtistaForm()
    
        return render(request,pag_api_busquedaForm,{"miFormulario":miFormulario})
    
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
    