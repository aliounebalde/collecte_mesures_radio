import datetime
import json
import os

from data_manager import DataManager

def load_config():
    """Charger la configuration"""
    try:
        with open("config.json",'r') as file:
           return json.load(file)
    except Exception as e:
        print(f"Erreur lors du chargement de la configuration : {e}")


def combine_measurements(wifi_file, distance_file):
    """
     Combine les mesures WiFi et les distances GPS en fonction du timestamp.
    :param wifi_file: Chemin du fichier JSON des mesures WiFi.
    :param distance_file: Chemin du fichier JSON des distances GPS.
    :param output_file: Chemin du fichier JSON de sortie.
    """
    config = load_config()
    data_manager = DataManager(config['output_dir'])
    wifi_data = data_manager.load_data(wifi_file)
    distance_data = data_manager.load_data(distance_file)
       
    # Créer un dictionnaire pour les distances GPS (timestamp -> distance)

    distance_dict ={item['timestamp'] : item['distance_m'] for item in distance_data}

    # Combiner les mesures WiFi avec les distances GPS
    combined_measurements = []

    for measurement in wifi_data['measurements']:
        timestamp = measurement['timestamp']
        if timestamp in distance_dict:
            measurement['distance_m'] = distance_dict[timestamp]
            combined_measurements.append(measurement)
        else:
            print(f"Avertissement : Aucune distance trouvée pour le timestamp {timestamp}")
    
    combined_data = {
        "metadata":wifi_data['metadata'],
        "measurements":combined_measurements
    }

    # Sauvegarder le nouveau fichier

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    output_file = os.path.join(config["output_dir"],f'results_{current_date}.json')
    
    data_manager.save_data(combined_data,output_file)

    print(f"Fichier JSON combiné sauvegardé sous : {output_file}")
    
if __name__ == '__main__':
    combine_measurements("results/results_00-01-36.json","results/distance_2025-02-20.json")