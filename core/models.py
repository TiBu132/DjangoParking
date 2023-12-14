from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True, verbose_name='Id de Usuario', null=False)
    nombre_usuario = models.CharField(max_length=50, verbose_name='Nombre del Usuario',null=True,blank=True, unique=True)
    pass_usuario = models.CharField(max_length=128, null=True, blank=True)
    pnombre = models.CharField(max_length=30,null=True,blank=True)
    ppaterno = models.CharField(max_length=30,null=True,blank=True)
    rut = models.CharField(max_length=30,null=True,blank=True)
    direccion = models.CharField(max_length=50,null=True,blank=True)
    num_casa = models.IntegerField(null=True, blank=True)
    patente_vehiculo = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f'{self.pnombre} {self.ppaterno}'
class tipoUsuario(models.Model):
    id_tipo = models.AutoField(primary_key=True, verbose_name="id_tipo")
    tipo_usuario = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return str(self.tipo_usuario)

    
class Vehiculo (models.Model):
    patente = models.CharField(primary_key=True, max_length=9, verbose_name='Patente del Vehiculo', db_column="Patente")
    marca = models.CharField(max_length=30, verbose_name='Marca del Vehiculo')
    modelo = models.CharField(max_length=30, verbose_name='Modelo  del Vehiculo')
    capacidad = models.IntegerField(null=True, blank=True)
    nombre_usuario = models.ForeignKey('Usuario', to_field="nombre_usuario", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.patente)
    
class Estacionamiento (models.Model):
    id_estacionamiento = models.AutoField(primary_key=True, verbose_name="id_estacionamiento")
    ubicacion = models.CharField(max_length=50, null=True, blank=True)
    costo = models.IntegerField(null=True, blank=True)
    patente = models.CharField(max_length=15,null=True, blank=True)
    nombre_usuario_duenno = models.ForeignKey('Usuario', on_delete=models.CASCADE, to_field="nombre_usuario", verbose_name="Nombre Dueño", null=True, blank=True, related_name="re_nombre_usuario_duenno")
    nombre_usuario_cliente = models.ForeignKey('Usuario', on_delete=models.CASCADE, to_field="nombre_usuario", verbose_name="Nombre Cliente", null=True, blank=True, related_name="re_nombre_usuario_cliente")
    espacio = models.CharField(max_length=10, null=True, blank=True)
    descripcion = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.id_estacionamiento)
    