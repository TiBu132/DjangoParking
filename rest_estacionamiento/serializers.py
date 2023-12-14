from rest_framework import serializers
from core.models import Usuario, Vehiculo, Estacionamiento

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["id_usuario","nombre_usuario","pass_usuario"]
        safe=False

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        safe=False

class EstacionamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estacionamiento
        fields = '__all__'
        safe=False
