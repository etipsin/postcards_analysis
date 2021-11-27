import ssl
import certifi
import geopy.geocoders
from geopy import distance
from geopy.geocoders import Nominatim

ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx


def get_address_by_coordinate(coord_x: float, coord_y: float):
    geo_locator = Nominatim(user_agent="user_agent")
    location = geo_locator.reverse(f"{coord_x}, {coord_y}", timeout=10)
    if location:
        return location.address

    return None


def get_region_by_coordinate(regions: list, coord: tuple):
    address = get_address_by_coordinate(coord_x=coord[0], coord_y=coord[1])
    if not address:
        return None

    address = address.lower()

    for reg in regions:
        if reg in address:
            return reg

    return None


def calculate_distance(coords_1: tuple, coords_2: tuple):
    return distance.distance(coords_1, coords_2).km
