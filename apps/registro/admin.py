from django.contrib import admin
from .models import Perfil,Planta,Reporte,SolicitudMantenimiento
# Register your models here.

admin.site.register(Perfil)
admin.site.register(Planta)
admin.site.register(Reporte)
admin.site.register(SolicitudMantenimiento)