from rest_framework.decorators import api_view
from rest_framework.response import Response

from .services.geo import geocode
from .services.routing import get_route
from .services.fuel import plan_optimal_fuel_stops, fuel_data
from django.core.cache import cache
import hashlib



@api_view(['POST'])
def route_fuel_plan(request):
    start = request.data.get("start")
    end = request.data.get("end")

    if not start or not end:
        return Response({"error": "start and end required"})

    # 🔥 Normalize input
    start_clean = start.strip().lower()
    end_clean = end.strip().lower()

    # 🔑 SAFE CACHE KEY (no warnings, production-safe)
    raw_key = f"{start_clean}_{end_clean}"
    cache_key = "route:" + hashlib.md5(raw_key.encode()).hexdigest()
    print("CACHE KEY USED:", cache_key)

    # ⚡ Check cache first
    cached_result = cache.get(cache_key)
    if cached_result:
        return Response(cached_result)

    # 📍 Geocode (1st external API)
    start_coords = geocode(start)
    end_coords = geocode(end)

    if not start_coords or not end_coords:
        return Response({"error": "invalid location"})

    # 🗺️ Routing API (2nd external API - allowed by requirement)
    route = get_route(start_coords, end_coords)

    distance = route["distance_miles"]
    geometry = route["geometry"]

    # ⛽ Fuel optimization logic
    fuel_stops, fuel_cost = plan_optimal_fuel_stops(
        distance,
        geometry,
        fuel_data
    )

    # 📦 Final response
    response_data = {
        "start": start,
        "end": end,
        "distance_miles": round(distance, 2),
        "route_map": geometry,
        "fuel_stops": fuel_stops,
        "total_fuel_cost": round(fuel_cost, 2)
    }

    # 💾 Cache result (1 hour)
    cache.set(cache_key, response_data, timeout=3600)

    return Response(response_data)