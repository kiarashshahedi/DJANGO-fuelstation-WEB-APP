from rest_framework import serializers
from .models import FuelStation, GasolineNozzle, GasNozzle, GasolineTank, GasTank

class FuelStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelStation
        fields = '__all__'

class GasolineNozzleSerializer(serializers.ModelSerializer):
    class Meta:
        model = GasolineNozzle
        fields = '__all__'

class GasNozzleSerializer(serializers.ModelSerializer):
    class Meta:
        model = GasNozzle
        fields = '__all__'

class GasolineTankSerializer(serializers.ModelSerializer):
    class Meta:
        model = GasolineTank
        fields = '__all__'

class GasTankSerializer(serializers.ModelSerializer):
    class Meta:
        model = GasTank
        fields = '__all__'
