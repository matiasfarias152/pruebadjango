
from clientes.models import Cliente
from django.db import models
from biblioteca.models import Libro

class Prestamo(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=255)
    multa = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    estado_devolucion = models.BooleanField(default=False)
    dias_multa = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id} - {self.libro.titulo} - {self.cliente.nombre}'

    def estado_devolucion_str(self):
        return "Devuelto" if self.estado_devolucion else "No devuelto"
    







   