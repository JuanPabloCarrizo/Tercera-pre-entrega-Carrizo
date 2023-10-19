# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class Avatar(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)    
    imagen = models.ImageField(upload_to='avatares/', null=True, blank= True)
    
    def __str__(self):
        return f"{settings.MEDIA_URL}{self.imagen}"
    
    # esto es para eliminar los archivos que se me juntaban en media, cada vez que actualizaba el avatar
    def save(self, *args, **kwargs):
        # Elimina el archivo anterior antes de guardar el nuevo
        try:
            this = Avatar.objects.get(id=self.id)
            if this.imagen != self.imagen:
                this.imagen.delete(save=False)
        except Avatar.DoesNotExist:
            pass

        super(Avatar, self).save(*args, **kwargs)
