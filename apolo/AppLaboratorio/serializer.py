from django.db import models
from django.db.models import fields
from AppLaboratorio.models import LabGiratorio

from rest_framework import serializers

class LabGiratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabGiratorio
        fields = '__all__'

    
