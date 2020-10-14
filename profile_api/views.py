from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profile_api import serializers


class PruebaApiView(APIView):
    "Sera la API view de Prueba"

    serializer_class = serializers.PruebaSerializers

    def get(self, request, format=None):
        "Retorna lista de caracteristicas del API view"
        an_apiview =[
            'Debiese devolverse todos los metodos como funciones',
            'No es tan distinta de una vista de django',
        ]

        return Response({'message': 'Holi', 'an_apiview': an_apiview})

    def post(self, request):
        "Se crea un mensaje con nuestro nombre"
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Holi {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method':'DELETE'})


# "El serializador se crea para recibir el contenido del post al api"