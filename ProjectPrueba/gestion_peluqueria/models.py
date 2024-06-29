from django.db import models

# Create your models here.

class Turno(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
  
    
    def __str__(self):
        texto = '{0} {1} {2}'
        return texto.format(self.nombre, self.fecha, self.hora)
