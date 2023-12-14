from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from core.models import Usuario, Estacionamiento, Vehiculo
from django.http import JsonResponse
from rest_estacionamiento.serializers import UsuarioSerializer, EstacionamientoSerializer, VehiculoSerializer
# Create your views here.

class UserView(APIView):
    def get(self, request):
        serializer = UsuarioSerializer(Usuario.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self, request):
        try:
            data = JSONParser().parse(request)
            usuario = data['usuario']
            password = data['pass']
            serializer = UsuarioSerializer(Usuario.objects.get(nombre_usuario = usuario, pass_usuario = password))
            return JsonResponse(serializer.data,safe=False)        
        except Usuario.DoesNotExist:
            return JsonResponse({'error': 'Credenciales inválidas'}, status=400, safe=False)
        except Exception as e:
            return JsonResponse(str(e), status=500, safe=False)

        
class RegisterView(APIView):
    def post(self,request):
        try:
            data = JSONParser().parse(request)
            Usuario.objects.create(
                nombre_usuario=data['nombre_usuario'],
                pass_usuario=data['pass_usuario'],
                pnombre=data['pnombre'],
                ppaterno=data['ppaterno'],
                rut=data['rut'],
                direccion=data['direccion'],
                num_casa=data['num_casa'],
            )

            return JsonResponse({"mensaje":"El Usuario se ha registrado exitosamente"}, status=200) 
        except Exception as e:
            return JsonResponse({'error': 'Error interno del servidor'}, status=500)
        
class EstacionamientoView(APIView):
    def get(self, request):
        serializer = EstacionamientoSerializer(Estacionamiento.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self, request):
        try:
            data = JSONParser().parse(request)

            Estacionamiento.objects.create(
                ubicacion=data['ubicacion'],
                costo=data['costo'],
                patente=data['patente'],
                nombre_usuario_duenno_id=data['nombre_usuario_dueño'],
                espacio=data['espacio'],
                descripcion=data['descripcion']
            )

            return JsonResponse({"mensaje": "El Viaje se ha registrado exitosamente"}, status=200)
        except Exception as e:
            print(f'Error en la vista: {repr(e)}')
            return JsonResponse(str(e), status=500, safe=False)

class VehiculoView(APIView):
    def get(self, request, nombre_usuario=None):
        if nombre_usuario is not None:
            print("Nombre de usuario recibido:", nombre_usuario)
            vehiculos = Vehiculo.objects.filter(nombre_usuario__nombre_usuario=nombre_usuario)
        else:
            vehiculos = Vehiculo.objects.all()

        serializer = VehiculoSerializer(vehiculos, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self,request):
        try:
            data = JSONParser().parse(request)
            Vehiculo.objects.create(
                patente=data['patente'],
                marca=data['marca'],
                modelo=data['modelo'],
                capacidad=data['capacidad'],
                nombre_usuario_id=data['nombre_usuario'],
            )
            return JsonResponse({"mensaje":"El Vehiculo se ha registrado exitosamente"}, status=200) 
        except Exception as e:
            return JsonResponse({'error': 'Error interno del servidor'},str(e), status=500)