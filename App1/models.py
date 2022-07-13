from django.db import models

# Create your models here.
class Mozo(models.Model):

    nombre=models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    antiguedad= models.DateField(default="2022-11-22")
    fecha_de_nacimiento= models.DateField(default="2022-11-22")

class Cocinero(models.Model):

    nombre=models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    antiguedad= models.DateField(default="2022-11-22")
    fecha_de_nacimiento= models.DateField(default="2022-11-22")

class LavaPlatos(models.Model):

    nombre=models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    antiguedad= models.DateField(default="2022-11-22")
    fecha_de_nacimiento= models.DateField(default="2022-11-22")