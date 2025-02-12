from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre = models.CharField(max_length = 30)
    telefono = models.CharField(max_length = 20)
    email = models.EmailField()

    def __str__(self):
        return (f" Nombre: {self.nombre}, Telefono: {self.telefono}, Email: {self.email}")
