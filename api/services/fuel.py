import math
import polyline
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "fuel_prices.csv")

fuel_data = pd.read_csv(CSV_PATH, sep="\t")

MAX_RANGE = 500
MPG = 10


def decode_route(geometry):
    coords = polyline.decode(geometry)
    return [(lat, lon) for lat, lon in coords]


def haversine(lat1, lon1, lat2, lon2):
    R = 3958.8

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)

    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda/2)**2
    return 2 * R * math.asin(math.sqrt(a))


def plan_optimal_fuel_stops(distance, geometry, fuel_data):

    coords = decode_route(geometry)
    if not coords:
        return [], 0

    fuel_data = fuel_data.copy().reset_index(drop=True)

    fuel_stops = []
    total_cost = 0

    num_stops = max(1, int(distance // MAX_RANGE))
    step = max(1, len(coords) // (num_stops + 1))

    for i in range(num_stops):

        idx = min((i + 1) * step, len(coords) - 1)

        # 🔥 take cheapest candidates
        candidates = fuel_data.nsmallest(5, "Retail Price")

        # deterministic selection (avoid randomness)
        station = candidates.iloc[i % len(candidates)]

        price = float(station["Retail Price"])
        gallons = MAX_RANGE / MPG
        cost = gallons * price

        fuel_stops.append({
            "location": f'{station["City"]}, {station["State"]}',
            "station": station["Truckstop Name"],
            "price_per_gallon": round(price, 2),
            "gallons": round(gallons, 2),
            "cost": round(cost, 2)
        })

        total_cost += cost

    return fuel_stops, round(total_cost, 2)