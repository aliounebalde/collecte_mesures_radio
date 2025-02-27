import numpy as np
import json

# Charger les données JSON
with open("results/final/simulation_wifi_realiste.json", 'r') as f:
    data = json.load(f)

# Extraire les distances (d) et les RSSI (Pr)
distances = [m['distance_m'] for m in data['measurements']]
rssi = [m['RSSI'] for m in data['measurements']]

# Distance de référence (d0)
d0 = 10  # outdoor

# Calculer x = log10(d / d0)
x = np.log10(np.array(distances) / d0)

# y = RSSI (Pr en dBm)
y = np.array(rssi)

# Méthode des moindres carrés pour trouver a et b
N = len(x)
a = (N * np.sum(x * y) - np.sum(x) * np.sum(y)) / (N * np.sum(x**2) - (np.sum(x))**2)
b = (np.sum(y) - a * np.sum(x)) / N

# Calculer gamma
gamma = -a / 10

# Calculer K (en supposant Pt = 20 dBm)
Pt = 20  # Puissance transmise en dBm
K = 10**(b / 10) / Pt

# Afficher les résultats
print(f"Gamma (γ) = {gamma}")
print(f"K = {K}")