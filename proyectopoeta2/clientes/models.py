from django.db import models
from django.core.validators import EmailValidator, MinValueValidator

class Cliente(models.Model):
    rut = models.CharField(max_length=20,unique=True)
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100, validators=[EmailValidator()])
    telefono = models.IntegerField(validators=[MinValueValidator(0)])
    direccion = models.CharField(max_length=200)
    multas = models.IntegerField(default=0, validators=[MinValueValidator(0)])

# Create your models here.

