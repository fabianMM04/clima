from django.contrib import admin
from .models import Medicion, Coordenadas, Ciudad, Historico

# Register your models here.
admin.site.register(Medicion)
admin.site.register(Coordenadas)
admin.site.register(Ciudad)
admin.site.register(Historico)
