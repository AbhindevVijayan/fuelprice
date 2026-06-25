import requests
from functools import lru_cache

@lru_cache(maxsize=1000)
def geocode(place):
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

    return (float(data[0]["lon"]), float(data[0]["lat"]))