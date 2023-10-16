from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User




class UserRegisterForm(UserCreationForm):
    
    username = forms.CharField()
    email = forms.EmailField(label='ingrese su email')
    first_name = forms.CharField()
    last_name = forms.CharField()
    password1 = forms.CharField(label='Ingrese una contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña',widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']
        help_text = {k: "" for k in fields}

class UserEditForm(forms.ModelForm):

    email = forms.EmailField(label="Ingrese su email:")    
    first_name = forms.CharField(label='ingrese su nombre')
    last_name = forms.CharField(label='ingrese su apellido')
    
    class Meta:
        model = User
        fields = ['email','first_name','last_name']
        help_text = {k: "" for k in fields}
        

class UserPasswordForm(forms.ModelForm):

    password1 = forms.CharField(label='Ingrese una contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña',widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['password1','password2',]
        help_text = {k: "" for k in fields}
        
        

        