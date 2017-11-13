import math


class defib():
    def __init__(self):
        self.id = None
        self.name = None
        self.address = None
        self.phone_number = None
        self.lon = None
        self.lat = None

    def string_to_defib(self, str_defib):
        str_defib = str_defib.split(';')

        self.id = str_defib[0]
        self.name = str_defib[1]
        self.address = str_defib[2]
        self.phone_number = str_defib[3]
        self.lon = str_defib[4]
        self.lat = str_defib[5]

        self.lon = float(self.lon.replace(',', '.'))
        self.lat = float(self.lat.replace(',', '.'))

def nearest_defibs(lon, lat, defibs):
    min_distance = 1000000
    closest_defib = None

    for item in defibs:
        unit = defib()
        unit.string_to_defib(item)
        distance = distance_to_defib(lon, lat, unit)
        if distance <= min_distance:
            closest_defib = unit
            min_distance = distance

    return closest_defib.name


def distance_to_defib(lon, lat, unit):
    lon = float(lon.replace(',', '.'))
    lat = float(lat.replace(',', '.'))

    x = (lon - unit.lon) * math.cos((unit.lat + lat)/2)

    y = (lat - unit.lat)

    return math.sqrt(x**2 + y**2) * 6371
