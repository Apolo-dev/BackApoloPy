from django.db import models
from django.db.models import fields
from AppLaboratorio.models import LabGiratorio, Energia

from rest_framework import serializers



class LabGiratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabGiratorio
        fields = '__all__'


class EnergiaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Energia
        fields = '__all__'
    

    
