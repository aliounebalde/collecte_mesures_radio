import json
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

# Charger le fichier JSON
with open("results/final/results_2025-02-26.json", "r") as file:
    data = json.load(file)

# Stocker les valeurs par distance
distance_dict = defaultdict(list)
rssi_dict = defaultdict(list)
debit_dict = defaultdict(list)

for measurement in data["measurements"]:
    distance = round(measurement["distance_m"])  # Arrondir pour grouper par distance entière
    distance_dict[distance].append(measurement["distance_m"])
    rssi_dict[distance].append(measurement["RSSI"])
    debit_dict[distance].append(measurement["Debit"])

# Calculer les moyennes
distances = sorted(distance_dict.keys())
mean_rssi = [np.mean(rssi_dict[d]) for d in distances]
mean_debit = [np.mean(debit_dict[d]) for d in distances]

# Tracer les courbes moyennées
plt.figure(figsize=(12, 5))

# Débit moyen vs Distance
plt.subplot(1, 2, 1)
plt.plot(distances, mean_debit, marker='o', linestyle='-', color='b', label="Débit moyen")
plt.xlabel("Distance (m)")
plt.ylabel("Débit moyen (Mbps)")
plt.title("Débit moyen en fonction de la distance")
plt.legend()
plt.grid()

# RSSI moyen vs Distance
plt.subplot(1, 2, 2)
plt.plot(distances, mean_rssi, marker='s', linestyle='-', color='r', label="RSSI moyen")
plt.xlabel("Distance (m)")
plt.ylabel("RSSI moyen (dBm)")
plt.title("Puissance reçue moyenne (RSSI) en fonction de la distance")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
