from django.db import models
from django.urls import reverse

class Tienda(models.Model):
    sucarsal = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)

    def __str__(self):
        return self.sucarsal

class Organizadores(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Juegos(models.Model):
    juego = models.CharField(max_length=200)
    edades = models.CharField(max_length=200)
    Organizadores = models.ForeignKey(
        Organizadores,
        on_delete=models.CASCADE,
    )

    Tienda = models.ForeignKey(
        Tienda,
        on_delete=models.CASCADE,
    )
    descripcion = models.TextField()
    foto = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.juego

    def get_absolute_url(self):
        return reverse('detalleJuego', args=[str(self.id)])


