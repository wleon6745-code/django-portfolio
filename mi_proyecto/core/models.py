from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio')
    url = models.URLField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Persona(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    titulo_academico = models.CharField(max_length=150)
    biografia = models.TextField()
    correo_electronico = models.EmailField()
    dedicacion_persona = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"