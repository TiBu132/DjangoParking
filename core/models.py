from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=30)
    pass_usuario = models.CharField(max_length=128, null=True, blank=True)
    pnombre = models.CharField(max_length=30,null=True,blank=True)
    ppaterno = models.CharField(max_length=30,null=True,blank=True)
    rut = models.CharField(max_length=30,null=True,blank=True)
    direccion = models.CharField(max_length=50,null=True,blank=True)
    num_casa = models.IntegerField(null=True, blank=True)

    def set_password(self, raw_password):
        # Almacena el hash de la contraseña
        self.pass_usuario = make_password(raw_password)

    def check_password(self, raw_password):
        # Verifica si la contraseña coincide con el hash almacenado
        return check_password(raw_password, self.pass_usuario)
class tipoUsuario(models.Model):
    id_tipo = models.AutoField(primary_key=True, verbose_name="id_tipo")
    tipo_usuario = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return str(self.tipo_usuario)
        