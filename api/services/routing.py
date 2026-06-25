import requests
from functools import lru_cache
ORS_API_KEY = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6ImEyMDJjMzkzOWRjYzQzZGRhZTg0MTY2YmIyM2ZlODIwIiwiaCI6Im11cm11cjY0In0="


@lru_cache(maxsize=1000)
def get_route(start_coords, end_coords):
    url = "https://api.openrouteservice.org/v2/directions/driving-car"

    headers = {
        "Authorization": ORS_API_KEY,
        "Content-Type": "application/json"
    }

    body = {
        "coordinates": [start_coords, end_coords]
    }

    r = requests.post(url, json=body, headers=headers)
    data = r.json()

    print("ORS RESPONSE:", data)

    if "routes" not in data:
        raise Exception(f"Routing API failed: {data}")

    route = data["routes"][0]

    return {
        "distance_miles": route["summary"]["distance"] / 1609.34,
        "geometry": route["geometry"]
    }