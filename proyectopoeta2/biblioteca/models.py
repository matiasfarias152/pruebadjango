from django.db import models

class Libro(models.Model):
    DISPONIBILIDAD_CHOICES = [
        ('disponible', 'Disponible'),
        ('no_disponible', 'No Disponible'),
    ]

    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    fecha = models.DateField()
    cantidad_total = models.PositiveIntegerField()
    genero = models.CharField(max_length=50)
    disponibilidad = models.CharField(max_length=15, choices=DISPONIBILIDAD_CHOICES, default='disponible')

    def save(self, *args, **kwargs):
        if self.cantidad_total == 0:
            self.disponibilidad = 'no_disponible'
        else:
            self.disponibilidad = 'disponible'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo
