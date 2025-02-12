import os
import json
import logging

class DataManager:
    """Classe pour gerer la sauvegarde"""
    def __init__(self, output_dir):
        self.output_dir = output_dir
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    def save_data(self,data, filename):
        """Sauvegarder les données dans un fichier JSON"""
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            logging.info(f"Données sauvegardées dans '{filename}'.")
        except Exception as e:
            logging.error(f"Erreur lors de la sauvegarde des données : {e}")

    def create_output_dir(self):
        """creer le dossier de sauvegarde du jour s'il n'existe pas"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            logging.info(f"Dossier '{self.output_dir}' créé.")