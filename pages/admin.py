from django.contrib import admin
from .models import *

# Register your models here.

class CiudadesAdmin(admin.ModelAdmin):
    admin.site.register(Ciudades)

class ZonasAdmin(admin.ModelAdmin):
    admin.site.register(Zonas)

class DistanciasAdmin(admin.ModelAdmin):
    admin.site.register(Distancias)

class ProveedoresAdmin(admin.ModelAdmin):
    admin.site.register(Proveedores)

class TarifasAdmin(admin.ModelAdmin):
    admin.site.register(Tarifas)
