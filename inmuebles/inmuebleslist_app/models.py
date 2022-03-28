from django.db import models

# Create your models here.


class Inmueble(models.Model):
    """ Propiedades (atributos) """
    direccion = models.CharField(max_length=250)
    pais = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=500)
    imagen = models.CharField(max_length=900)
    activo = models.BooleanField(default=True)

    # índice (dirección como índice - toString)
    def __str__(self):
        return self.direccion
