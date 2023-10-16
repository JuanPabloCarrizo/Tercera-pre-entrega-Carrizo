from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# class UserRegisterForm(UserCreationForm):
#     username = forms.CharField()
#     email = forms.EmailField()
#     password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
#     password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    
#     class Meta:
#         model = User
#         fields = ['username','email','password1','password2']
#         help_text = {k:"" for k in fields}

class ArtistaFormulario(forms.Form):
    nombre = forms.CharField(required=True)
    nacionalidad = forms.CharField(required=True)
    fechaNac = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'DD/MM/AAAA'}),
        input_formats=['%d/%m/%Y'],
        help_text='Formato: DD/MM/AAAA'
    )
    fechaFallecimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'DD/MM/AAAA'}),
        input_formats=['%d/%m/%Y'],
        help_text='Formato: DD/MM/AAAA'
    )
    movimiento = forms.CharField(required=True)
    
class ObraFormulario(forms.Form):
    nombre=forms.CharField(required=True)
    autor=forms.CharField(required=True)
    anio=forms.IntegerField(label="Año",required=True)
    ubicacion=forms.CharField(label="Ubicación", required=True)
    material=forms.CharField(required=True)
    
class GaleriaFormulario(forms.Form):
    nombre=forms.CharField(required=True)
    ubicacion=forms.CharField(label="Ubicación", required=True)
    obras=forms.CharField(required=True)
    
class BuscarArtistaForm(forms.Form):
    nombre=forms.CharField(required=True)

class BuscarObraForm(forms.Form):
    nombre=forms.CharField(required=True)
    
class BuscarGaleriaForm(forms.Form):
    nombre=forms.CharField(required=True)
    
