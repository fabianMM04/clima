from django.db import models
from django.utils import timezone

# Create your models here.

class Medicion(models.Model):
    temp = models.IntegerField(verbose_name='Temperatura', default=0)
    humedad = models.IntegerField(verbose_name="Humedad", default=0)
    viento = models.CharField(verbose_name="Viento", max_length=20)
    desc = models.CharField(verbose_name="Descripcion", max_length=100)
    fcs = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{}|{}|{}|{}|{}".format(self.temp, self.humedad, self.viento, self.desc, self.fcs)


class Coordenadas(models.Model):
    lat = models.IntegerField(verbose_name="Latitud", default=0)
    lon = models.IntegerField(verbose_name="Longitud", default=0)
    fcs = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{}|{}|{}".format(self.lat, self.lon, self.fcs)


class Sensor(models.Model):
    tipo = models.CharField(verbose_name="Tipo", max_length=20)
    est = models.BooleanField(default=False)
    medicion_id = models.OneToOneField(Medicion, verbose_name="Medicion")
    coor_id = models.OneToOneField(Coordenadas, verbose_name="Coordenadas")
    fcs = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{}|{}|{}|{}|{}".format(self.tip, self.est, self.fcs)
