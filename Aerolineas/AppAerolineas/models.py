from django.db import models

# Create your models here.
class Aeropuertos(models.Model):
    nombre = models.CharField(max_length=50)
    siglas = models.CharField(max_length=5)
    pais = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    internacional = models.CharField(max_length=5)
    año_inauguracion = models.IntegerField()

class Aerolineas(models.Model):
    nombre = models.CharField(max_length=50)
    siglas = models.CharField(max_length=10)
    sede = models.CharField(max_length=50)
    alianza = models.CharField(max_length=50)
    año_fundacion = models.IntegerField()

class Vuelos(models.Model):
    aerolinea_siglas = models.CharField(max_length=10)
    vuelo_numero = models.CharField(max_length=10)
    fecha_vuelo = models.DateField()
    hora_vuelo = models.IntegerField()
    aeropuerto_origen = models.CharField(max_length=5)
    aeropuerto_destino = models.CharField(max_length=5)
    duracion_vuelo = models.IntegerField()