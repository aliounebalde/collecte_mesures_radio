import json
import subprocess
from math import radians, sin, cos, sqrt, atan2

# Calcul de distance avec la formule de Haversine


def haversine(lat1, lon1, lat2, lon2):
    R = 6371000  # Rayon de la Terre en mètres
    phi1, phi2 = radians(lat1), radians(lat2)
    delta_phi = radians(lat2 - lat1)
    delta_lambda = radians(lon2 - lon1)
    a = sin(delta_phi / 2)**2 + cos(phi1) * \
        cos(phi2) * sin(delta_lambda / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c


# Point de départ
start_lat, start_lon = 48.8566, 2.3522  # Exemple : Paris

# Liste des positions testées
positions = [
    (48.8584, 2.2945),
    (48.8606, 2.3376),   # Musée du Louvre
    (48.8738, 2.2950),    # Sacré-Cœur
    (48.8600, 2.3280),    # Notre-Dame de Paris
    (48.8351, 2.3086),     # Parc des Princes
    (48.8967, 2.3185)     # Stade de France

]

# Liste des résultats
measurements = []

# Simulation de collecte de données pour chaque position
for lat, lon in positions:
    distance = haversine(start_lat, start_lon, lat, lon)
    print(distance)
    # Commande iperf (exemple)
   # throughput = subprocess.run(["iperf3", "-c", "192.168.1.1", "-u", "-b", "10M"],
    #                             capture_output = True, text = True)
    # Supposons des valeurs simulées ici
    rssi = -50 + int(distance / 100)  # RSSI simulé
    latency = 15 + int(distance / 100)  # Latence simulée
    packet_loss = 0.01 * int(distance / 100)  # Perte simulée

    # Ajouter aux mesures
    measurements.append({
        "distance_m": round(distance, 2),
        "rssi_dBm": rssi,
        "throughput_Mbps": 10,  # Simulé
        "latency_ms": latency,
        "packet_loss": packet_loss
    })

# Enregistrement dans un fichier JSON
with open('results.json', 'w') as f:
    json.dump({"measurements": measurements}, f, indent=4)

print("Données collectées et enregistrées dans 'results.json'.")
