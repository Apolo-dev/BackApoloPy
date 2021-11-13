from rest_framework.fields import JSONField
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

    wi = queryset[0].wi
    f80 = queryset[0].f80
    p80 = queryset[0].p80

    def calcular(self):
        res = (10*self.wi)*((1/sqrt(self.p80))-(1/sqrt(self.f80)))
        energia = round(res, 2)

        diccionario = [{"energy": energia}]
        print(diccionario)
        return (energia)


class CalcEnegy(Energia):

    def algo(self):
        return self.calcular()


rsss = CalcEnegy()
print(rsss.algo())
    
        
    
        


