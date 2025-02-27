import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Charger les données du fichier JSON
file_path = "results/final/results_2025-02-26.json"  # Remplace par le chemin correct si nécessaire
with open(file_path, "r") as file:
    data = json.load(file)

# Extraire les mesures en DataFrame
df = pd.DataFrame(data["measurements"])

# Trier les données par distance croissante
df = df.sort_values(by="distance_m")

# Appliquer un filtre de lissage (moyenne glissante)
window_size = 3  # Fenêtre de lissage
df["RSSI_smooth"] = df["RSSI"].rolling(window=window_size, center=True).mean()
df["Debit_smooth"] = df["Debit"].rolling(window=window_size, center=True).mean()

# Tracer les graphiques après lissage
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Courbe débit moyen
axes[0].plot(df["distance_m"], df["Debit"], 'bo-', alpha=0.4, label="Débit brut")
axes[0].plot(df["distance_m"], df["Debit_smooth"], 'b-', label="Débit lissé")
axes[0].set_xlabel("Distance (m)")
axes[0].set_ylabel("Débit (Mbps)")
axes[0].set_title("Débit moyen en fonction de la distance")
axes[0].legend()
axes[0].grid(True)

# Courbe RSSI moyen
axes[1].plot(df["distance_m"], df["RSSI"], 'rs-', alpha=0.4, label="RSSI brut")
axes[1].plot(df["distance_m"], df["RSSI_smooth"], 'r-', label="RSSI lissé")
axes[1].set_xlabel("Distance (m)")
axes[1].set_ylabel("RSSI moyen (dBm)")
axes[1].set_title("Puissance reçue moyenne (RSSI) en fonction de la distance")
axes[1].legend()
axes[1].grid(True)

# Afficher les graphiques
plt.tight_layout()
plt.show()