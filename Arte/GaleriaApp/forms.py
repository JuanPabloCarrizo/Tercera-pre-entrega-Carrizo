from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from GaleriaApp.models import Comentario, Artista, Galeria, Obra

    
class ArtistaFormulario(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ["nombre", "cita", "nacionalidad", "fechaNac", "fechaFallecimiento", "movimiento", "biografia", "foto"]
        widgets = {
            'fechaNac': forms.DateInput(attrs={'type': 'date'}),
            'fechaFallecimiento': forms.DateInput(attrs={'type': 'date'}),
        }
    
class ObraFormulario(forms.Form):
    nombre=forms.CharField(required=True)
    cita = forms.CharField(required=True)
    autor=forms.CharField(required=True)
    anio=forms.IntegerField(label="Año",required=True)
    # ubicacion=forms.CharField(label="Ubicación", required=True)
    material=forms.CharField(required=True)
    biografia = forms.CharField(required=True)
    foto = forms.ImageField(required=True)
    artista = forms.ModelChoiceField(queryset=Artista.objects.all(), empty_label=None)
    galeria = forms.ModelChoiceField(queryset=Galeria.objects.all(), empty_label=None)
    
class GaleriaFormulario(forms.Form):
    nombre=forms.CharField(required=True)
    cita = forms.CharField(required=True)
    ubicacion=forms.CharField(label="Ubicación", required=True)
    biografia = forms.CharField(required=True)
    foto = forms.ImageField(required=True)
    
    
    
class BuscarArtistaForm(forms.Form):
    nombre=forms.CharField(required=True)

class BuscarObraForm(forms.Form):
    nombre=forms.CharField(required=True)
    
class BuscarGaleriaForm(forms.Form):
    nombre=forms.CharField(required=True)
    
    
# form para los comentarios de los usuarios
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
    
