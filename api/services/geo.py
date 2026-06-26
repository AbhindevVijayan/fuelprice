import requests
from django.core.cache import caches

cache = caches["geo"]

def geocode(place):
    print("🔥 CALLING GEOCODE API") 
    cache_key = f"geo:{place.lower().strip()}"

    cached = cache.get(cache_key)
    if cached:
        return cached

    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": place,
        "format": "json"
    }

    headers = {
        "User-Agent": "fuel-planner-app"
    }

    r = requests.get(url, params=params, headers=headers)
    data = r.json()

    print("GEOCODE RESPONSE:", place, data)

    if not data:
        return None

    result = (float(data[0]["lon"]), float(data[0]["lat"]))

    cache.set(cache_key, result)

    return result