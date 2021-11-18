from django.urls import path, include
from rest_framework.fields import JSONField, SerializerMethodField

#from Pokemon.AppPrincipal.models import Ataque
from .views import SaveLab, Energia, CalcEnegy, saveAbertura
from rest_framework import routers


router = routers.DefaultRouter()
router.register('pesos', SaveLab)
router.register('aberturas', saveAbertura)
router.register('energia', Energia)
#router.register('calculos', CalcEnegy)

urlpatterns=[
    path('', include(router.urls)),
]