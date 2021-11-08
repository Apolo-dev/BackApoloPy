from django.db.models import query
from django.shortcuts import render
#from rest_framework.views import APIView
from .serializer import LabGiratorioSerializer
from rest_framework.response import Response
from .models import LabGiratorio
from rest_framework import status
from rest_framework import viewsets

# Create your views here.

class SaveLab(viewsets.ModelViewSet):
    queryset = LabGiratorio.objects.all()
    serializer_class = LabGiratorioSerializer
    





    