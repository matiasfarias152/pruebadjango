from django.contrib import admin
from .models import Prestamo

class PrestamoAdmin(admin.ModelAdmin):
    list_display = ['id', 'fecha_prestamo', 'fecha_devolucion', 'estado', 'multa', 'libro', 'cliente', 'estado_devolucion', 'dias_multa']

admin.site.register(Prestamo, PrestamoAdmin)