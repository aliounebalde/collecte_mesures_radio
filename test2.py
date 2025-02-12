from math import radians, sin, cos, sqrt, atan2


def haversine(lat1, lon1, lat2, lon2):
    R = 6371000  # Rayon de la Terre en mètres
    phi1, phi2 = radians(lat1), radians(lat2)
    delta_phi = radians(lat2 - lat1)
    delta_lambda = radians(lon2 - lon1)
    a = sin(delta_phi / 2)**2 + cos(phi1) * \
        cos(phi2) * sin(delta_lambda / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c


lat = 48.95751057
lon = 2.29636303
lat2 = 48.95754117
lon2 = 2.29661769
lat3 = 48.95771588
lon3 = 2.29664389

# print(haversine(lat, lon, lat2, lon2))
print(haversine(lat, lon, lat3, lon3))
positions = []
with open("20250208-182840.txt") as file:
    for line in file:
        if line.startswith("W"):
            parts = line.split(",")
            latitude = parts[2]
            longitude = parts[3]
            positions.append((latitude, longitude))

print(positions)
