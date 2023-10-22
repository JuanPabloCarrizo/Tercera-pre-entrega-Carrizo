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
        
    def clean_foto(self):
        foto = self.cleaned_data.get('foto')
        if not foto:
            raise forms.ValidationError("El campo 'foto' es requerido.")
        return foto
    

class ObraFormulario(forms.ModelForm):
    artista = forms.ModelChoiceField(
        queryset=Artista.objects.all(),
        empty_label=None,  # Esto eliminará la etiqueta vacía
    )
    galeria = forms.ModelChoiceField(
        queryset=Galeria.objects.all(),
        empty_label=None,  # Esto eliminará la etiqueta vacía
    )

    class Meta:
        model = Obra
        fields = ["nombre", "cita", "anio", "material", "biografia", "foto", "artista", "galeria"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['artista'].widget.attrs.update({'class': 'mi-clase-css'})
        self.fields['galeria'].widget.attrs.update({'class': 'mi-otra-clase-css'})
        
    def clean_foto(self):
        foto = self.cleaned_data.get('foto')
        if not foto:
            raise forms.ValidationError("El campo 'foto' es requerido.")
        return foto
 
    
class GaleriaFormulario(forms.ModelForm):
    class Meta:
        model = Galeria
        fields = ["nombre", "cita", "ubicacion","biografia", "foto"]
        
    def clean_foto(self):
        foto = self.cleaned_data.get('foto')
        if not foto:
            raise forms.ValidationError("El campo 'foto' es requerido.")
        return foto
     
    
# form para los comentarios de los usuarios
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
    
