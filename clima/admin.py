from django.contrib import admin
from .models import Medicion, Coordenadas, Sensor

# Register your models here.
admin.site.register(Medicion)
admin.site.register(Coordenadas)
admin.site.register(Sensor)
