import datetime
import time
import json
from Wifi_metrics import WifiMetricsCollector
from data_manager import DataManager
import os


def load_config():
    """Charger la configuration"""
    try:
        with open("config.json",'r') as file:
           return json.load(file)
    except Exception as e:
        print(f"Erreur lors du chargement de la configuration : {e}")

def main():
    config = load_config()
    wifi_collector = WifiMetricsCollector(config["interface"])
    data_manager = DataManager(config["output_dir"])

    data_manager.create_output_dir()

    # Obtenir la date actuelle pour créer un dossier par jour
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Obtenir la date et l'heure actuelles pour le nom du fichier
    current_time = datetime.datetime.now().strftime("%H-%M-%S")

    # Créer un nom de fichier unique dans le dossier
    filename = os.path.join(config["output_dir"], f"measurement_{current_time}.json")
    measurements = []
    #output_dir = f"results_{current_date}"
    start_time = time.time()
    while(time.time() - start_time < config["duration_seconds"]):
        
        wifi_metrics = wifi_collector.get_wifi_metrics()

        wifi_metrics["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        
        # Ajouter la mesure à la liste
        measurements.append(wifi_metrics)

        time.sleep(config["collecte_interval_seconds"])
    data = {
    "metadata": {
        "start_date": current_time,
        "environment": "outdoor",
        "network_type": "WiFi",
        "device": "Raspberry Pi 4"
    },
    "measurements": measurements
    }
    data_manager.save_data(data,filename)

if __name__ == "__main__":
    main()