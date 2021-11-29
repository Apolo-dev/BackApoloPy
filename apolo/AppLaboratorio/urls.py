from django.urls import path, include
from .views import SaveDetailAbertura, SaveLab, SaveDetailLab, saveAbertura
#from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
#from snippets import views


urlpatterns = [
    path('pesos/', SaveLab.as_view()),
    path('pesos/<str:pk>/', SaveDetailLab.as_view()),
    path('aberturas/', saveAbertura.as_view()),
    path('aberturas/<str:pk>/', SaveDetailAbertura.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)