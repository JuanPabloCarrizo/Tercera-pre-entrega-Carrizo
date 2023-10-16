# Create your models here.

from django.contrib.auth.models import User
from django.db import models

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
    
#     avatar = models.ImageField(upload_to='avatars/', null=True, blank= True)
    # Otros campos para perfiles

class Avatar(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank= True)
    
    def __str__(self):
        return f"{self.user} - {self.imagen}"
    
