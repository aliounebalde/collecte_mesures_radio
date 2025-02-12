import os
import json
import datetime
import time

class DataManager:
    """Classe pour gerer la sauvegarde"""
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def save_data(self,data, filename):
        """Sauvegarder les données dans un fichier JSON"""
        with open(filename,'r') as file:
            json.dump(data,file,indent=4)

    def create_output_dir(self):
        """creer le dossier de sauvegarde du jour s'il n'existe pas"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            