from django import forms
from django.contrib import admin
from .models import Libro

class LibroAdminForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'

class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'fecha', 'cantidad_total', 'genero', 'disponibilidad']
    list_filter = ['disponibilidad']
    form = LibroAdminForm

admin.site.register(Libro, LibroAdmin)