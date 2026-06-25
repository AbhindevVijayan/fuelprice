import polyline
import math


def decode_route(encoded_geometry):
    """
    Convert ORS encoded geometry into coordinates
    """

    return polyline.decode(encoded_geometry)



def get_route_checkpoints(points, distance_miles):
    """
    Select approximate fuel stop points every 500 miles
    """

    checkpoints = []

    total_points = len(points)

    stops = math.ceil(distance_miles / 500)

    interval = max(
        1,
        total_points // stops
    )

    for i in range(0, total_points, interval):
        checkpoints.append(points[i])

    return checkpoints[:stops]