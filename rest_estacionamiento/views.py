from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from core.models import Usuario
from django.http import JsonResponse
from rest_estacionamiento.serializers import UsuarioSerializer
# Create your views here.

class UserView(APIView):
    def get(self, request):
        serializer = UsuarioSerializer(Usuario.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self, request):
        try:
            usuario = request.data['usuario']
            password = request.data['pass']
            serializer = UsuarioSerializer(Usuario.objects.get(nombre_usuario = usuario, pass_usuario = password))

            return JsonResponse(serializer.data,safe=False)        
        except Usuario.DoesNotExist:
            return JsonResponse({'error': 'Credenciales inválidas'}, status=400)
        except Exception as e:
            return JsonResponse(str(e), status=500)

        
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
        
        
