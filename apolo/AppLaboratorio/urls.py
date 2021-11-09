from django.urls import path, include

#from Pokemon.AppPrincipal.models import Ataque
from .views import SaveLab, Energia
from rest_framework import routers


router = routers.DefaultRouter()
router.register('pesos', SaveLab)
router.register('energia', Energia)

urlpatterns=[
    path('', include(router.urls)),
]