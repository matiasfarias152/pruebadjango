from django.db import models
from django.core.validators import EmailValidator, MinValueValidator
from django.core.exceptions import ValidationError

class Cliente(models.Model):
    rut = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100, validators=[EmailValidator()])
    telefono = models.IntegerField(validators=[MinValueValidator(0)])
    direccion = models.CharField(max_length=200)
    multas = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.nombre

    def clean(self):
        # Validar el RUT
        if not self.rut:
            raise ValidationError("El RUT no puede estar vacío.")
        
        rut_clean = self.rut.replace(".", "").replace("-", "").lower()
        
        if not rut_clean[:-1].isdigit() or not (rut_clean[-1].isdigit() or rut_clean[-1] == 'k'):
            raise ValidationError("Formato de RUT incorrecto. Ejemplo válido: 12345678-9.")

        if len(rut_clean) not in [9, 10]:
            raise ValidationError("Longitud de RUT incorrecta. Ejemplo válido: 12345678-9 o 21192454-3.")

        # Validar el teléfono
        if self.telefono is not None and (self.telefono < 100 or len(str(self.telefono)) < 3):
            raise ValidationError("Número de teléfono inválido. Debe tener al menos 3 dígitos.")