from django.urls import path, include
#from rest_framework.fields import JSONField, SerializerMethodField

#from Pokemon.AppPrincipal.models import Ataque
from .views import SaveLab, SaveDetailLab
#from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
#from snippets import views


urlpatterns = [
    path('pesos/', SaveLab.as_view()),
    path('pesos/<int:pk>/', SaveDetailLab.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)