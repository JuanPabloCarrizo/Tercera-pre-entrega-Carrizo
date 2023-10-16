from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView , PasswordChangeView
from django.views.generic.edit import CreateView, UpdateView
from .models import UserProfile
from Usuarios.forms import UserRegisterForm , UserPasswordForm #Esto es para registro
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from Usuarios.forms import UserEditForm
from django.urls import reverse_lazy




# Create your views here.
plantillas = {
    'inicio': 'GaleriaApp/inicio.html',
    'login' : 'users/login.html',
    'register' : 'users/register.html',
    'edit' : 'users/edit.html',
    'password': 'users/change_password.html',
}

# Vistas de login, logout y registro.
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
       
        miFormulario = UserEditForm(request.POST)
        
        if miFormulario.is_valid():
           
            informacion = miFormulario.cleaned_data
            
            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
                
            usuario.save()
                
                
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


    
