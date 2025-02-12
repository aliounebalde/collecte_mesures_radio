
import datetime
import os
import subprocess
import re
# Objectif:
# recuperer la puissance du signal wifi, debit, SNR
# sauvegarder les données dans un fichier json en ajoutant des metadata (date, heure, etc.)
# creer un dossier pour stocker les résultats par date (s'il n'existe pas déjà)

measurements = {}
metadata = {}
current_date = datetime.datetime.now().strftime("%Y-%m-%d")
output_dir = f"results_{current_date}"

if not os.path.exists(output_dir):
    os.mkdir(output_dir)


def get_measurements(interface):
    result = subprocess.run(["iw", "dev", interface, "station", "dump"],
                            capture_output=True, text=True)
    if result.returncode == 0:
        for line in result.stdout.split("\n"):
            match_rssi = re.search(r"signal:\s+(-?\d+)", line)
            if match_rssi:
                measurements["rssi"] = match_rssi.group(1)
