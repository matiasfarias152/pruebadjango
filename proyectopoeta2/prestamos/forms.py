from django import forms
from .models import Prestamo

class PrestamoForm(forms.ModelForm):
    class Meta:
        ESTADO_CHOICES = [
            ('mal_estado', 'Mal estado'),
            ('normal', 'Normal'),
            ('buen_estado', 'Buen estado'),
        ]

        model = Prestamo
        fields = ['fecha_prestamo', 'fecha_devolucion', 'estado', 'multa', 'libro', 'cliente', 'estado_devolucion', 'dias_multa']
        widgets = {
            'fecha_prestamo': forms.DateInput(attrs={'type': 'date'}),
            'fecha_devolucion': forms.DateInput(attrs={'type': 'date'}),
            'estado': forms.Select(choices=ESTADO_CHOICES),
            'estado_devolucion': forms.CheckboxInput(),
         
        }

    def clean(self):
        cleaned_data = super().clean()
        fecha_prestamo = cleaned_data.get('fecha_prestamo')
        fecha_devolucion = cleaned_data.get('fecha_devolucion')
        multa = cleaned_data.get('multa')
        dias_multa = cleaned_data.get('dias_multa')

        if not fecha_prestamo:
            raise forms.ValidationError("La fecha de préstamo no puede estar vacía.")

        if not fecha_devolucion:
            raise forms.ValidationError("La fecha de devolución no puede estar vacía.")

        if  multa is None:
            raise forms.ValidationError("La multa no puede estar vacía.")

        if fecha_devolucion and fecha_prestamo and fecha_devolucion < fecha_prestamo:
            raise forms.ValidationError("La fecha de devolución no puede ser anterior a la fecha de préstamo.")

        if multa < 0:
            raise forms.ValidationError("La multa no puede ser menor a 0.")

        if dias_multa is None:
            raise forms.ValidationError("Los días de multa no pueden ser nulos.")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Deshabilita el campo estado_devolucion al crear un nuevo préstamo
        if not self.instance.pk:
            self.fields['estado_devolucion'].widget.attrs['disabled'] = True
