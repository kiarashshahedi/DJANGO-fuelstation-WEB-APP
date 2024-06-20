from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.dateparse import parse_datetime


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

class SyncDataView(APIView):
    def get(self, request, *args, **kwargs):
        last_sync = request.query_params.get('last_sync')
        if last_sync:
            last_sync = parse_datetime(last_sync)
            stations = FuelStation.objects.filter(last_modified__gt=last_sync)
        else:
            stations = FuelStation.objects.all()
        serializer = FuelStationSerializer(stations, many=True)
        return Response(serializer.data)