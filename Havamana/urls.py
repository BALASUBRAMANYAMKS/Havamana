from django.urls import path
from .views import get_weather, search, reverse_geocode

urlpatterns = [
    path('', search, name='search'),
    path('weather/', get_weather, name='weather_dashboard'),
    path('api/reverse-geocode/', reverse_geocode, name='reverse_geocode'),
]
