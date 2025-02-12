import os
import json
import datetime
import time
#from math import radians, sin, cos, sqrt, atan2
import subprocess
import re
# Fonction pour calculer la distance (exemple)

# def haversine(lat1, lon1, lat2, lon2):
#     R = 6371000  # Rayon de la Terre en mètres
#     phi1, phi2 = radians(lat1), radians(lat2)
#     delta_phi = radians(lat2 - lat1)
#     delta_lambda = radians(lon2 - lon1)
#     a = sin(delta_phi / 2)**2 + cos(phi1) * \
#         cos(phi2) * sin(delta_lambda / 2)**2
#     c = 2 * atan2(sqrt(a), sqrt(1 - a))
#     return R * c

# Fonction pour obtenir le RSSI (exemple)

def get_wifi_metrics(interface="wlp0s20f3"):
    """Récupère le RSSI, le SNR et le débit de l'interface Wi-Fi."""
    metrics = {
        "RSSI": None,  # Niveau de signal en dBm
        "SNR": None,   # Rapport Signal/Bruit en dB
        "Debit": None  # Débit en Mbps
    }

    
    try:
        result = subprocess.run(["iw", "dev", interface, "station", "dump"], capture_output=True, text=True)
        if result.returncode == 0:
            for line in result.stdout.split("\n"):
                # Cherche le RSSI (Signal Level)
                match_rssi = re.search(r"signal:\s+(-?\d+)", line)
                if match_rssi:
                    metrics["RSSI"] = int(match_rssi.group(1))

                # Cherche le débit
                match_bitrate = re.search(r"rx bitrate:\s+([\d.]+)", line)
                if match_bitrate:
                    metrics["Débit"] = float(match_bitrate.group(1))
    except Exception as e:
        print("Erreur lors de l'exécution de iw dev :", e)

    # 2️⃣ Récupérer le SNR avec `/proc/net/wireless`
    try:
        result = subprocess.run(["cat", "/proc/net/wireless"], capture_output=True, text=True)
        if result.returncode == 0:
            for line in result.stdout.split("\n"):
                if interface in line:
                    values = line.split()
                    signal_level = float(values[2])  # RSSI en dBm
                    noise_level = float(values[3])  # Niveau de bruit en dBm
                    metrics["SNR"] = signal_level - noise_level  # Calcul du SNR
    except Exception as e:
        print("Erreur lors de l'exécution de /proc/net/wireless :", e)

    return metrics


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
measurements = []
def collect_data_continuously(duration_seconds=300): #collecte pendant 5min 
    start_time = time.time()
    while(time.time() - start_time < duration_seconds):
        wifi_metrics = get_wifi_metrics()

        wifi_metrics["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        
        # Ajouter la mesure à la liste
        measurements.append(wifi_metrics)

        time.sleep(10)

collect_data_continuously()
# Structurer les données avec des métadonnées
data = {
    "metadata": {
        "start_date": current_time,
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
