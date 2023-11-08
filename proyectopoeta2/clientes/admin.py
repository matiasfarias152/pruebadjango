from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Cliente

class  ClienteAdmin(admin.ModelAdmin):
    list_display = ['rut','nombre','correo','telefono','direccion','multas']

admin.site.register(Cliente, ClienteAdmin)