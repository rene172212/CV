from django.db import models

# Create your models here.
class experiencia(models.Model):
    nombre_empresa = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField(max_length=1000)

class educacion(models.Model):
    nombre_institucion = models.CharField(max_length=100)
    titulo_obtenido = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField(max_length=1000)

class idiomas(models.Model):
    nombre_idioma = models.CharField(max_length=100)
    nivel = models.ForeignKey('nivel', on_delete=models.CASCADE)  

class nivel(models.Model):
    nombre_nivel = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=1000)    