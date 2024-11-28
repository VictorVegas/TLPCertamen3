from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta

# Funcion de validacion de fecha.
def validar_fecha(value):
    if value < datetime.now().date():
        raise ValidationError('La fecha no puede ser en el pasado')
    elif value > datetime.now().date() + timedelta(days=365*5):
        raise ValidationError('La fecha no puede ser ingresada tantos años en el futuro')

class TipoEvento(models.Model):
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre

# modelo de evento simple: nombre, fecha, tipos y descripcion del evento.
class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateField(
        validators=[validar_fecha]
    )
    
    tipos = models.JSONField(default=list, blank=True)
    
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre