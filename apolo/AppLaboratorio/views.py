from .serializer import LabGiratorioSerializer, EnergiaSerializer
from .models import LabGiratorio, Energia
from rest_framework import routers, viewsets

# matematicas
from math import sqrt


# Create your views here.

class SaveLab(viewsets.ModelViewSet):
    queryset = LabGiratorio.objects.all()
    serializer_class = LabGiratorioSerializer


class Energia(viewsets.ModelViewSet):
    queryset = Energia.objects.all()
    serializer_class = EnergiaSerializer

# POO

    wi = queryset[0].wi
    f80 = queryset[0].f80
    p80 = queryset[0].p80

    

    res = (10*wi)*((1/sqrt(p80))-(1/sqrt(f80)))
    energia = round(res, 2)

    diccionario = {"energy": energia}


    print(diccionario)
    print(energia)

    

    





    