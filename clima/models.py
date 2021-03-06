from django.db import models
from django.utils import timezone

# Create your models here.

class Medicion(models.Model):
    temp = models.IntegerField(verbose_name='Temperatura', default=0)
    humedad = models.IntegerField(verbose_name="Humedad", default=0)
    uv = models.CharField(verbose_name="Rayo uv", max_length=20)
    pres = models.IntegerField(verbose_name="Presion", default=0)
    s_ter = models.IntegerField(verbose_name="Sensacion Termica", default=0)
    desc = models.CharField(verbose_name="Descripcion", max_length=100)
    fec = models.CharField(verbose_name="Fecha", max_length=100)

    def __str__(self):
        return "{}|{}|{}|{}|{}".format(self.temp, self.humedad, self.uv, self.desc, self.fec)


class Coordenadas(models.Model):
    lat = models.IntegerField(verbose_name="Latitud", default=0)
    lon = models.IntegerField(verbose_name="Longitud", default=0)

    def __str__(self):
        return "{}|{}".format(self.lat, self.lon)

class Ciudad(models.Model):
    nom = models.CharField(verbose_name="Ciudad", max_length=20)

    def __str__(self):
        return "{}|{}".format(self.lat, self.lon)

class Historico(models.Model):
    ciu_id = models.OneToOneField(Ciudad, verbose_name="Ciudad")
    medicion_id = models.OneToOneField(Medicion, verbose_name="Medicion")
    coor_id = models.OneToOneField(Coordenadas, verbose_name="Coordenadas")

    def __str__(self):
        return "{}|{}|{}".format(self.ciu_id, self.medicion_id, self.coor_id)
