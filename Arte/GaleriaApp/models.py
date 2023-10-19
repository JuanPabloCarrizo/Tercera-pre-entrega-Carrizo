from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Artista(models.Model):
    nombre=models.CharField(max_length=40)
    cita = models.CharField(max_length=500, null=True, blank=True)
    nacionalidad=models.CharField(max_length=100)
    fechaNac=models.DateField()
    fechaFallecimiento=models.DateField()
    movimiento=models.CharField(max_length=100)
    biografia = models.CharField(max_length=1500, null=True, blank=True)
    foto = models.ImageField(upload_to='artistas', null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.nombre}"
    
    def obras_en_artista(self):
        return self.obra_set.all()  
    
    # esto es para eliminar los archivos que se me juntaban en media, cada vez que actualizaba el avatar
    def save(self, *args, **kwargs):
        # Elimina el archivo anterior antes de guardar el nuevo
        try:
            this = Artista.objects.get(id=self.id)
            if this.foto != self.foto:
                this.foto.delete(save=False)
        except Artista.DoesNotExist:
            pass

        super(Artista, self).save(*args, **kwargs)
         
class Galeria(models.Model):
    nombre=models.CharField(max_length=100)
    cita = models.CharField(max_length=500, null=True, blank=True)
    ubicacion=models.CharField(max_length=200)
    biografia = models.CharField(max_length=1500, null=True, blank=True)
    foto = models.ImageField(upload_to='galerias', null=True, blank=True)    

    
    def obras_en_galeria(self):
        return self.obras_set.all()  
    
    
    def __str__(self):
        return f"{self.nombre}" 
    
    # esto es para eliminar los archivos que se me juntaban en media, cada vez que actualizaba el avatar
    def save(self, *args, **kwargs):
        # Elimina el archivo anterior antes de guardar el nuevo
        try:
            this = Galeria.objects.get(id=self.id)
            if this.foto != self.foto:
                this.foto.delete(save=False)
        except Galeria.DoesNotExist:
            pass

        super(Galeria, self).save(*args, **kwargs)
    

class Obra(models.Model):
    nombre=models.CharField(max_length=100)
    cita=models.CharField(max_length=500, null=True, blank=True)
    anio=models.IntegerField()
    material=models.CharField(max_length=200)
    biografia = models.CharField(max_length=1500, null=True, blank=True)
    foto = models.ImageField(upload_to='obras',null=True, blank=True)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='obras',null=False)
    galeria = models.ForeignKey(Galeria, on_delete=models.CASCADE, related_name='obras',null=False)

    
    def __str__(self):
        return f"{self.nombre}"
    
    # esto es para eliminar los archivos que se me juntaban en media, cada vez que actualizaba el avatar
    def save(self, *args, **kwargs):
        # Elimina el archivo anterior antes de guardar el nuevo
        try:
            this = Obra.objects.get(id=self.id)
            if this.foto != self.foto:
                this.foto.delete(save=False)
        except Obra.DoesNotExist:
            pass

        super(Obra, self).save(*args, **kwargs)


class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE, related_name='comentarios_obra', null=True, blank=True)
    galeria = models.ForeignKey(Galeria, on_delete=models.CASCADE, related_name='comentarios_galeria', null=True, blank=True)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='comentarios_artista', null=True, blank=True)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.usuario} - {self.fecha}"

