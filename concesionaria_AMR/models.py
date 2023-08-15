from django.db import models

# Create your models here.

class Car(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()

class Customer(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

class Sale(models.Model):
    coche = models.ForeignKey(Car, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Customer, on_delete=models.CASCADE)
    fecha = models.DateField()
