from rest_framework import generics
from .models import FuelStation, GasolineNozzle, GasNozzle, GasolineTank, GasTank
from .serializers import FuelStationSerializer, GasolineNozzleSerializer, GasNozzleSerializer, GasolineTankSerializer, GasTankSerializer

class FuelStationListCreate(generics.ListCreateAPIView):
    queryset = FuelStation.objects.all()
    serializer_class = FuelStationSerializer

class FuelStationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FuelStation.objects.all()
    serializer_class = FuelStationSerializer

class GasolineNozzleListCreate(generics.ListCreateAPIView):
    queryset = GasolineNozzle.objects.all()
    serializer_class = GasolineNozzleSerializer

class GasolineNozzleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GasolineNozzle.objects.all()
    serializer_class = GasolineNozzleSerializer

class GasNozzleListCreate(generics.ListCreateAPIView):
    queryset = GasNozzle.objects.all()
    serializer_class = GasNozzleSerializer

class GasNozzleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GasNozzle.objects.all()
    serializer_class = GasNozzleSerializer

class GasolineTankListCreate(generics.ListCreateAPIView):
    queryset = GasolineTank.objects.all()
    serializer_class = GasolineTankSerializer

class GasolineTankDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GasolineTank.objects.all()
    serializer_class = GasolineTankSerializer

class GasTankListCreate(generics.ListCreateAPIView):
    queryset = GasTank.objects.all()
    serializer_class = GasTankSerializer

class GasTankDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GasTank.objects.all()
    serializer_class = GasTankSerializer
