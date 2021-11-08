from django.urls import path, include

#from Pokemon.AppPrincipal.models import Ataque
from .views import SaveLab
from rest_framework import routers


router = routers.DefaultRouter()
router.register('pesos', SaveLab)

urlpatterns=[
    path('', include(router.urls)),
]