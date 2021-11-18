from AppLaboratorio.models import LabGiratorio, Energia, Abertura

from rest_framework import serializers



class LabGiratorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabGiratorio
        fields = '__all__'

class AberturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abertura
        fields = '__all__'


class EnergiaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Energia
        fields = '__all__'
    

    