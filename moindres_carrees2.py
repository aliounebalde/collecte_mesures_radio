import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Charger les données du fichier JSON
file_path = "results/final/simulation_wifi_realiste.json"  # Remplace par le chemin correct si nécessaire
with open(file_path, "r") as file:
    data = json.load(file)

# Extraire les mesures en DataFrame
df = pd.DataFrame(data["measurements"])

# Trier les données par distance croissante
df = df.sort_values(by="distance_m")

# Filtrer les distances supérieures à d0 (10m en outdoor)
d0 = 10  # Distance de référence en mètres
df_filtered = df[df["distance_m"] >= d0]

# Conversion des valeurs pour la régression linéaire
log_d = np.log10(df_filtered["distance_m"])  # log(distance)
Pr = df_filtered["RSSI"]  # Puissance reçue en dBm

# Régression linéaire
slope, intercept, r_value, p_value, std_err = linregress(log_d, Pr)

gamma = -slope  # gamma est l'opposé de la pente
K = intercept  # Intercept représente K directement

# Tracer les résultats
plt.figure(figsize=(12, 6))
plt.scatter(log_d, Pr, label="Données mesurées", color="blue")
plt.plot(log_d, intercept + slope * log_d, color="red", label=f"Régression linéaire (gamma={gamma:.2f})")
plt.xlabel("log10(Distance)")
plt.ylabel("Puissance reçue (dBm)")
plt.legend()
plt.grid(True)
plt.title("Régression linéaire du modèle de propagation")
plt.show()

# Afficher les valeurs de gamma et K
print(f"Gamma estimé: {gamma:.2f}")
print(f"K estimé: {K:.2f} dBm")