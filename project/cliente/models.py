from django.db import models

class pais(models.Model):
    nombre = models.CharField(max_length=100, unique=True)


class cliente(models.Model):
    nombre = models.CharField(max_length=100),
    apellido = models.CharField(max_length=100),
    nacimiento = models.DateField(null=True, blank=True)
    pais_origen = models.ForeignKey(pais, on_delete=models.SET_NULL, null=True, blank=True)
