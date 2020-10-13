from rest_framework.views import APIView
from rest_framework.response import Response

class PruebaApiview(APIView):
    "Sera la API view de Prueba"

    def get(self, request, format=None):
        "Retorna lista de caracteristicas del API view"
        an_apiview =[
            'Debiese devolverse tosos los metodos como funciones'
        ]

        return Response({'message': 'Holi', 'an_apiview': an_apiview})