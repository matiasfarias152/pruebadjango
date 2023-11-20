from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'fecha', 'cantidad_total', 'genero']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        titulo = cleaned_data.get('titulo')
        autor = cleaned_data.get('autor')
        fecha = cleaned_data.get('fecha')
        cantidad_total = cleaned_data.get('cantidad_total')
        genero = cleaned_data.get('genero')

        if not titulo or not autor or not fecha or genero is None:
            raise ValidationError("Ninguno de los campos puede estar vacío.")
        
        if fecha > timezone.now().date():
            raise ValidationError("La fecha no puede ser en el futuro.")

        if cantidad_total is not None and cantidad_total < 0:
            raise ValidationError("La cantidad total no puede ser negativa.")