from django.db import models

# Create your models here.
class Aeropuertos(models.Model):
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=5)
    pais = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    internacional = models.CharField(max_length=5)
    año_inauguracion = models.IntegerField()

    def __str__(self):
        return f'NOMBRE: {self.nombre} ({self.siglas})  ➜  PAIS: {self.pais}  ➜  PROVINCIA: {self.estado}  ➜  INTERNACIONAL: {self.internacional}  ➜  AÑO: {self.año_inauguracion}'



class Aerolineas(models.Model):
    nombre = models.CharField(max_length=50)
    siglas = models.CharField(max_length=10)
    sede = models.CharField(max_length=50)
    alianza = models.CharField(max_length=50)
    año_fundacion = models.IntegerField()

    def __str__(self):
        return f'NOMBRE: {self.nombre} ({self.siglas})  ➜  PAIS: {self.sede}  ➜  ALIANZA: {self.alianza}  ➜  AÑO: {self.año_fundacion}'



class Vuelos(models.Model):
    aerolinea_siglas = models.CharField(max_length=10)
    vuelo_numero = models.CharField(max_length=10)
    fecha_vuelo = models.DateField()
    hora_vuelo = models.IntegerField()
    aeropuerto_origen = models.CharField(max_length=5)
    aeropuerto_destino = models.CharField(max_length=5)
    duracion_vuelo = models.IntegerField()

    def __str__(self):
        return f'VUELO: {self.aerolinea_siglas}-{self.vuelo_numero}  ➜  FECHA: {self.fecha_vuelo}  ➜  HORA: {self.hora_vuelo}  ➜  ORIGEN: {self.aeropuerto_origen}  ➜  DESTINO: {self.aeropuerto_destino}  ➜  DURACION: {self.duracion_vuelo}'