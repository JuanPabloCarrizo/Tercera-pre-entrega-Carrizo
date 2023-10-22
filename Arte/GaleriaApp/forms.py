from django import forms
from GaleriaApp.models import Comentario, Artista, Galeria, Obra

    
class ArtistaFormulario(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ["nombre", "cita", "nacionalidad", "fechaNac", "fechaFallecimiento", "movimiento", "biografia", "foto"]
        widgets = {
            'fechaNac': forms.DateInput(attrs={'type': 'date'}),
            'fechaFallecimiento': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'nombre': 'Nombre del Artista',
            'cita': 'Cita',
            'nacionalidad': 'Nacionalidad',
            'fechaNac': 'Fecha de Nacimiento',
            'fechaFallecimiento': 'Fecha de Fallecimiento',
            'movimiento': 'Movimiento Artístico',
            'biografia': 'Biografía',
            'foto': 'Foto del Artista',
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
        
        labels = {
            'nombre': 'Nombre de la Obra',
            'cita': 'Cita',
            'anio': 'Año de Creación',
            'material': 'Material Utilizado',
            'biografia': 'Biografía de la Obra',
            'foto': 'Foto de la Obra',
            'artista': 'Artista Relacionado',
            'galeria': 'Galería de Exhibición',
        }

    # Aplico cambios para que se vea mejor los combos de selección en el formulario!
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
        labels = {
            'nombre': 'Nombre de la Galería',
            'cita': 'Cita',
            'ubicacion': 'Ubicación',
            'biografia': 'Biografía de la Galería',
            'foto': 'Foto de la Galería',
        }
        
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
    
