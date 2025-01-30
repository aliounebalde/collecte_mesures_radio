import os
import json
import datetime
import time

# Fonction pour calculer la distance (exemple)


def calculate_distance():
    return 100.5  # Simulé

# Fonction pour obtenir le RSSI (exemple)


def get_wifi_rssi():
    return -60  # Simulé

# Fonction pour obtenir le débit (exemple)


def get_throughput():
    return 10.2  # Simulé

# Fonction pour obtenir la latence (exemple)


def get_latency():
    return 20.1  # Simulé

# Fonction pour obtenir la perte de paquets (exemple)


def get_packet_loss():
    return 0.01  # Simulé


# Obtenir la date actuelle pour créer un dossier par jour
current_date = datetime.datetime.now().strftime("%Y-%m-%d")

# Créer un dossier pour stocker les résultats (s'il n'existe pas déjà)
output_dir = f"results_{current_date}"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Obtenir la date et l'heure actuelles pour le nom du fichier
current_time = datetime.datetime.now().strftime("%H-%M-%S")

# Créer un nom de fichier unique dans le dossier
filename = os.path.join(output_dir, f"results_{current_time}.json")

# Simuler des mesures
measurements = [
    {
        "distance_m": calculate_distance(),
        "rssi_dBm": get_wifi_rssi(),
        "throughput_Mbps": get_throughput(),
        "latency_ms": get_latency(),
        "packet_loss": get_packet_loss()
    }
]

# Structurer les données avec des métadonnées
data = {
    "metadata": {
        "date": current_time,
        "environment": "outdoor",
        "network_type": "WiFi",
        "device": "Raspberry Pi 4"
    },
    "measurements": measurements
}

# Sauvegarder les données dans le fichier
with open(filename, 'w') as f:
    json.dump(data, f, indent=4)

print(f"Données collectées et enregistrées dans '{filename}'.")
