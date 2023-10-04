from django import forms


class ArtistaFormulario(forms.Form):
    nombre=forms.CharField(required=True)
    nacionalidad=forms.CharField(required=True)
    fechaNac=forms.DateField(label="Fecha de nacimiento",required=True,input_formats=['%d/%m/%Y'],help_text="dd/mm/yyyy")
    fechaFallecimiento=forms.DateField(label="Fecha de fallecimiento",required=True,input_formats=['%d/%m/%Y'],help_text="dd/mm/yyyy")
    movimiento=forms.CharField(required=True)
    
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