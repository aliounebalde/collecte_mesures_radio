import json
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Charger le fichier JSON
with open("results/final/simulation_wifi_realiste.json", "r") as file:
    data = json.load(file)

# Extraction des distances et RSSI
distances = np.array([entry['distance_m'] for entry in data['measurements']])
puissance_recue = np.array([entry["RSSI"] for entry in data['measurements']])  # RSSI en dBm
print(distances)
log_d = np.log10(distances)  # log10 de la distance

# Régression linéaire
slope, intercept, _, _, _ = linregress(log_d, puissance_recue)
gamma = -slope / 10  # gamma = - pente de la droite

print(f"Valeur estimée de gamma: {gamma:.2f}")

# Tracé des résultats
plt.scatter(log_d, puissance_recue, label="Données mesurées")
plt.plot(log_d, slope * log_d + intercept, color='red', label=f"Régression linéaire (gamma={gamma:.2f})")
plt.xlabel("log10(Distance)")
plt.ylabel("Puissance reçue (dBm)")  # Correction du label
plt.legend()
plt.show()

# Calcul de K
d0 = 10  # Distance de référence en mètres
Pt = 20  # ⚠️ Remplace par la vraie puissance transmise en dBm
Pr_d0 = puissance_recue[np.argmin(np.abs(distances - d0))]  # RSSI le plus proche de d0

#K = 10 ** ((Pr_d0 - Pt + 10 * gamma * np.log10(d0)) / 10)
K = intercept
print(f"Valeur estimée de K : {K:.2f}")
