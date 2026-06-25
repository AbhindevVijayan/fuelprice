from django.urls import path
from .views import route_fuel_plan

urlpatterns = [
    path("route-fuel-plan/", route_fuel_plan),
]