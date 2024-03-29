from rest_framework.fields import DateField, JSONField
from rest_framework.views import APIView
from .serializer import LabGiratorioSerializer, EnergiaSerializer, AberturaSerializer
from .models import LabGiratorio, Energia, Abertura
from rest_framework import routers, viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# matematicas
from math import sqrt


# Create your views here.

class SaveLab(APIView):


    def get(self, request, format=None):
        queryset = LabGiratorio.objects.all()
        serializer_class = LabGiratorioSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def post(self, request, format=None):
        serializer = LabGiratorioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SaveDetailLab(APIView):

    def get_object(self, pk):
        try:
            return LabGiratorio.objects.get(fechaActual=pk)
        except LabGiratorio.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pesos = self.get_object(pk)
        serializer = LabGiratorioSerializer(pesos)
        #print(pesos)
        return Response(serializer.data)


# class Calculo(SaveDetailLab):
#     print(get())



# modelo de abertura
class saveAbertura(APIView):
    def get(self, request, format=None):
        queryset = Abertura.objects.all()
        serializer_class = AberturaSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def post(self, request, format=None):
        serializer = AberturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SaveDetailAbertura(APIView):

    def get_object(self, pk):
        try:
            return Abertura.objects.get(fechaActual=pk)
        except Abertura.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Aberturas = self.get_object(pk)
        serializer = AberturaSerializer(Aberturas)
        return Response(serializer.data)



