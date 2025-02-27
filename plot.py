import json
import matplotlib.pyplot as plt

# Charger le fichier JSON
with open("results/final/results_2025-02-26.json", "r") as file:
    data = json.load(file)

# Extraire les données
distances = []
debits = []
rssi_values = []

for measurement in data["measurements"]:
    distances.append(measurement["distance_m"])
    debits.append(measurement["Debit"])
    rssi_values.append(measurement["RSSI"])

# Tracer les graphes
plt.figure(figsize=(12, 5))

# Débit vs Distance
plt.subplot(1, 2, 1)
plt.plot(distances, debits, marker='o', linestyle='-', color='b', label="Débit")
plt.xlabel("Distance (m)")
plt.ylabel("Débit (Mbps)")
plt.title("Débit en fonction de la distance")
plt.legend()
plt.grid()

# RSSI vs Distance
plt.subplot(1, 2, 2)
plt.plot(distances, rssi_values, marker='s', linestyle='-', color='r', label="RSSI")
plt.xlabel("Distance (m)")
plt.ylabel("RSSI (dBm)")
plt.title("Puissance reçue (RSSI) en fonction de la distance")
plt.legend()
plt.grid()

# Afficher les graphes
plt.tight_layout()
plt.show()
