from rest_framework.decorators import api_view
from rest_framework.response import Response

from .services.geo import geocode
from .services.routing import get_route
from .services.fuel import plan_optimal_fuel_stops, fuel_data
from django.core.cache import cache


@api_view(['POST'])
def route_fuel_plan(request):
    start = request.data.get("start")
    end = request.data.get("end")

    if not start or not end:
        return Response({"error": "start and end required"})

    # 🔥 CACHE KEY (normalize input)
    cache_key = f"route:{start.strip().lower()}_{end.strip().lower()}"
    cached_result = cache.get(cache_key)

    # ✅ RETURN FAST RESPONSE IF EXISTS
    if cached_result:
        return Response(cached_result)

    start_coords = geocode(start)
    end_coords = geocode(end)

    if not start_coords or not end_coords:
        return Response({"error": "invalid location"})

    route = get_route(start_coords, end_coords)

    distance = route["distance_miles"]
    geometry = route["geometry"]

    fuel_stops, fuel_cost = plan_optimal_fuel_stops(
        distance,
        geometry,
        fuel_data
    )

    response_data = {
        "start": start,
        "end": end,
        "distance_miles": distance,
        "route_map": geometry,
        "fuel_stops": fuel_stops,
        "total_fuel_cost": fuel_cost
    }

    # 🔥 STORE RESULT IN CACHE (1 hour)
    cache.set(cache_key, response_data, timeout=3600)

    return Response(response_data)