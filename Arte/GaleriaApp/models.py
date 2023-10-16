from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Artista(models.Model):
    nombre=models.CharField(max_length=40)
    # cita = models.CharField(max_length=100)
    nacionalidad=models.CharField(max_length=40)
    fechaNac=models.DateField()
    fechaFallecimiento=models.DateField()
    movimiento=models.CharField(max_length=40)
    #biografia = models.CharField(max_length=500)
    #obras = models.CharField(max_length =500)
    # foto = models.ImageField(upload_to='artistas/')
    # autorPost = models.CharField()
    # fechaPost = models.DateField()
    # comentarios = models.CharField()
    
    
    def __str__(self):
        return f"{self.nombre} - {self.nacionalidad} - {self.fechaNac} - {self.fechaFallecimiento} - {self.movimiento}"
         
class Galeria(models.Model):
    nombre=models.CharField(max_length=100)
    # cita = models.CharField(max_length=100)
    ubicacion=models.CharField(max_length=100)
    obras=models.CharField(max_length=300)
   # biografia = models.CharField(max_length=500)
    #foto = models.ImageField(upload_to='artistas/')    
    # def obras_en_galeria(self):
    #     return self.obras_set.all()
    # autorPost= models.CharField()
    # fechaPost = models.DateField()
    # comentarios = models.CharField()
    
    
    
    def __str__(self):
        return f"{self.nombre} - {self.ubicacion} - {self.obras}" 
    

class Obra(models.Model):
    nombre=models.CharField(max_length=100)
    # cita=models.CharField()
    autor=models.CharField(max_length=40)
    anio=models.CharField(max_length=4)
    ubicacion=models.CharField(max_length=100)
    material=models.CharField(max_length=100)
    # biografia = models.CharField(max_length=500)
    # artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    # galeria = models.ForeignKey(Galeria, on_delete=models.CASCADE)
        # autorPost= models.CharField()
    # fechaPost = models.DateField()
    # comentarios = models.CharField()
    
    
    def __str__(self):
        return f"{self.nombre} - {self.autor} - {self.anio} - {self.ubicacion} - {self.material}"




# class Comentario(models.Model):
#     usuario = models.ForeignKey(User, on_delete=models.CASCADE)
#     obra = models.ForeignKey(Obra, on_delete=models.CASCADE, related_name='comentarios_obra')
#     galeria = models.ForeignKey(Galeria, on_delete=models.CASCADE, related_name='comentarios_galeria', null=True, blank=True)
#     artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='comentarios_artista', null=True, blank=True)
#     texto = models.TextField()
#     fecha = models.DateTimeField(auto_now_add=True)

