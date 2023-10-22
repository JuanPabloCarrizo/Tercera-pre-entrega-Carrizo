from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from Usuarios.forms import UserRegisterForm , UserPasswordForm #Esto es para registro
from django.contrib.auth.decorators import login_required
from Usuarios.forms import UserEditForm, User
from Usuarios.models import Avatar
from django.core.files.storage import default_storage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from GaleriaApp.models import Obra, Galeria, Artista  # Importa los modelos de tu aplicación
from django.views.generic import ListView
from django.views.generic.edit import DeleteView

# Create your views here.
plantillas = {
    'inicio': 'GaleriaApp/inicio.html',
    'login' : 'users/login.html',
    'register' : 'users/register.html',
    'edit' : 'users/edit.html',
    'password': 'users/change_password.html',
    'crear_usuario' : 'users/crear_usuario.html',
    'usuario_list':'users/usuario_list.html',
    'usuario_confirm_delete': 'users/usuario_confirm_delete.html',
}

# registro.
# log in y out, lo manejo desde urls.py
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')  
    else:
        form = UserRegisterForm()

    return render(request, plantillas['register'], {'form': form})

@login_required
def edit(request):

    usuario = request.user

    
    if request.method == 'POST':
       
        miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario)

        
        if miFormulario.is_valid():
           
            informacion = miFormulario.cleaned_data
            
            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
                
            usuario.save()

            nueva_imagen = informacion.get('imagen', None)
            if nueva_imagen is not None:
                try:
                    avatar = Avatar.objects.get(user=usuario)
                except Avatar.DoesNotExist:
                    # Si no existe un avatar, crea uno nuevo
                    avatar = Avatar(user=usuario, imagen=nueva_imagen)
                else:
                    # Si el avatar ya existe, actualiza la imagen
                    avatar.imagen = nueva_imagen

                # Antes de guardar el nuevo avatar
                if avatar.imagen:
                    # Elimina el archivo del avatar anterior
                    default_storage.delete(avatar.imagen.path)
                avatar.save()
                                
            return redirect('Inicio')  
    
    else:
        miFormulario = UserEditForm(instance=usuario)
    
    return render(request, plantillas['edit'], {"mi_form": miFormulario})

@login_required
def ChangePassword(request):

    usuario = request.user
    
    if request.method == 'POST':
       
        miFormulario = UserPasswordForm(request.POST)
        
        if miFormulario.is_valid():
           
            informacion = miFormulario.cleaned_data

            if informacion['password1'] != informacion['password2']:
                datos = {
                    'msj_error':"Las contraseñas no coinciden"
                }
            
                miFormulario = UserPasswordForm(datos)
                
            else:
                usuario.set_password(informacion['password1'])
                usuario.save()
                
                return redirect('Inicio')                         
    
    else:

        miFormulario = UserPasswordForm(initial={'password': usuario.password,})

    
    return render(request, plantillas['password'], {"mi_form": miFormulario})

from django.contrib.auth.models import User

@login_required
def crear_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()  # Guarda el usuario en la base de datos

            # Asignar permisos para Obra
            content_type_obra = ContentType.objects.get_for_model(Obra)
            permisos_obra = Permission.objects.filter(content_type=content_type_obra)

            # Asignar permisos para Galeria
            content_type_galeria = ContentType.objects.get_for_model(Galeria)
            permisos_galeria = Permission.objects.filter(content_type=content_type_galeria)

            # Asignar permisos para Artista
            content_type_artista = ContentType.objects.get_for_model(Artista)
            permisos_artista = Permission.objects.filter(content_type=content_type_artista)

            # Agregar permisos para los tres tipos de modelos
            permisos = list(permisos_obra) + list(permisos_galeria) + list(permisos_artista)
            usuario.user_permissions.set(permisos)  # Usar 'set' para establecer los permisos

            # Configurar el usuario como is_staff
            usuario.is_staff = True

            # Finalmente, guardar el usuario nuevamente para actualizar permisos y is_staff
            usuario.save()

            return redirect('Listar-Usuarios')
    else:
        form = UserCreationForm()
    return render(request, plantillas['crear_usuario'], {'form': form})


# Muestro todos los usuarios 
class UserListView(ListView):
    model = User
    template_name = plantillas['usuario_list']
    context_object_name = 'users'

    
class UserDeleteView(DeleteView):
    model = User
    template_name = plantillas['usuario_confirm_delete']
    success_url = reverse_lazy('Listar-Usuarios')
    
