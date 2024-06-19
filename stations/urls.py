from django.urls import path
from .views import create_station, station_list, station_detail, generate_pdf_reportlab

from stations.views_api import (
    FuelStationListCreate, FuelStationDetail,
    GasolineNozzleListCreate, GasolineNozzleDetail,
    GasNozzleListCreate, GasNozzleDetail,
    GasolineTankListCreate, GasolineTankDetail,
    GasTankListCreate, GasTankDetail
)






urlpatterns = [
    
    path('', station_list, name='station_list'),
    path('new/', create_station, name='create_station'),
    path('<int:pk>/', station_detail, name='station_detail'),
    path('PDF/<int:pk>/', generate_pdf_reportlab, name='generate_pdf_reportlab'),
    
    # API
    path('api/stations/', FuelStationListCreate.as_view(), name='station-list-create'),
    path('api/stations/<int:pk>/', FuelStationDetail.as_view(), name='station-detail'),
    path('api/gasoline_nozzles/', GasolineNozzleListCreate.as_view(), name='gasoline-nozzle-list-create'),
    path('api/gasoline_nozzles/<int:pk>/', GasolineNozzleDetail.as_view(), name='gasoline-nozzle-detail'),
    path('api/gas_nozzles/', GasNozzleListCreate.as_view(), name='gas-nozzle-list-create'),
    path('api/gas_nozzles/<int:pk>/', GasNozzleDetail.as_view(), name='gas-nozzle-detail'),
    path('api/gasoline_tanks/', GasolineTankListCreate.as_view(), name='gasoline-tank-list-create'),
    path('api/gasoline_tanks/<int:pk>/', GasolineTankDetail.as_view(), name='gasoline-tank-detail'),
    path('api/gas_tanks/', GasTankListCreate.as_view(), name='gas-tank-list-create'),
    path('api/gas_tanks/<int:pk>/', GasTankDetail.as_view(), name='gas-tank-detail'),

]
