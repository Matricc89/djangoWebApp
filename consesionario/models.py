from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
   

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.edad}"

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    

    def __str__(self):
        return f"{self.nombre} {self.direccion} "

class Auto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    color = models.CharField(max_length=100,null=True, blank=True)
    precio = models.IntegerField()
    

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.color} {self.precio} "

