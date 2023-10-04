from django.db import models

# Create your models here.
class Artista(models.Model):
    nombre=models.CharField(max_length=40)
    nacionalidad=models.CharField(max_length=40)
    fechaNac=models.DateField()
    fechaFallecimiento=models.DateField()
    movimiento=models.CharField(max_length=40)
     
class Obra(models.Model):
    nombre=models.CharField(max_length=100)
    autor=models.CharField(max_length=40)
    anio=models.CharField(max_length=4)
    ubicacion=models.CharField(max_length=100)
    material=models.CharField(max_length=100)
    
class Galeria(models.Model):
    nombre=models.CharField(max_length=100)
    ubicacion=models.CharField(max_length=100)
    obras=models.CharField(max_length=300)
    
    