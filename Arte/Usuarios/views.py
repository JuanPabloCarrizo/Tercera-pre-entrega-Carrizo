from django.shortcuts import render, redirect
from Usuarios.forms import UserRegisterForm , UserPasswordForm #Esto es para registro
from django.contrib.auth.decorators import login_required
from Usuarios.forms import UserEditForm
from Usuarios.models import Avatar
from django.core.files.storage import default_storage





# Create your views here.
plantillas = {
    'inicio': 'GaleriaApp/inicio.html',
    'login' : 'users/login.html',
    'register' : 'users/register.html',
    'edit' : 'users/edit.html',
    'password': 'users/change_password.html',
    'page_not_found': 'users/page_not_found.html',
}

def page_not_found(request, exception):

    return render(request, plantillas['page_not_found'], status=404)


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
       
        miFormulario = UserEditForm(request.POST, request.FILES)
        
        if miFormulario.is_valid():
           
            informacion = miFormulario.cleaned_data
            
            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
                
            usuario.save()

            #esto graba en la tabla Avatar
            imagen = informacion['imagen']
            try:
                avatar = Avatar.objects.get(user=usuario)
            except Avatar.DoesNotExist:
                # Si no existe un avatar, crea uno nuevo
                avatar = Avatar(user=usuario, imagen=imagen)
            else:
                # Si el avatar ya existe, actualiza la imagen
                avatar.imagen = imagen
                
            # Antes de guardar el nuevo avatar
            if usuario.avatar:
                print("ENTRA EN USUARIO AVATAR")
                # Elimina el archivo del avatar anterior
                default_storage.delete(avatar.imagen.path)    
                print(f'tiene: {avatar.imagen.path}')

            avatar.save()
                
                
            return redirect('Inicio')  
    
    else:

        miFormulario = UserEditForm(initial={'email': usuario.email,
                                                'first_name': usuario.first_name,
                                                'last_name': usuario.last_name,})

    
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


    
