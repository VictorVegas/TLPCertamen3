from django.db import models


# modelo de evento
class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateField()
    descripcion = models.TextField()
    inicio = models.TimeField()
    fin = models.TimeField()

    def __str__(self):
        return self.nombre