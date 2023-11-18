from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    fecha = models.DateField()
    cantidad = models.PositiveIntegerField()
    disponibilidad = models.BooleanField(default=True)
    genero = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo
