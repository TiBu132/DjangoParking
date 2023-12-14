from django.contrib import admin
from .models import Usuario, tipoUsuario, Vehiculo, Estacionamiento
# Register your models here.

admin.site.register(Usuario)
admin.site.register(tipoUsuario)
admin.site.register(Vehiculo)
admin.site.register(Estacionamiento)