from django import forms
from .models import Prestamo

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['fecha_prestamo', 'fecha_devolucion', 'estado', 'multa', 'libro', 'cliente', 'estado_devolucion', 'dias_multa']
        widgets = {
            'fecha_prestamo': forms.DateInput(attrs={'type': 'date'}),
            'fecha_devolucion': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        fecha_prestamo = cleaned_data.get('fecha_prestamo')
        fecha_devolucion = cleaned_data.get('fecha_devolucion')

        if fecha_devolucion and fecha_prestamo and fecha_devolucion < fecha_prestamo:
            raise forms.ValidationError("La fecha de devolución no puede ser anterior a la fecha de préstamo.")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Deshabilita el campo estado_devolucion al crear un nuevo préstamo
        if not self.instance.pk:
            self.fields['estado_devolucion'].widget.attrs['disabled'] = True