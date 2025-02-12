import subprocess
import re

class WifiMetrics:
    """Classe pour collecter les métriques WiFi (RSSI, SNR, débit)."""
    def __init__(self,interface):
        self.interface = interface

    def get_wifi_metrics(self):
        """Récupère le RSSI, le SNR et le débit de l'interface Wi-Fi."""
    
        metrics = {
            "RSSI": None,  # Niveau de signal en dBm
            "SNR": None,   # Rapport Signal/Bruit en dB
            "Debit": None  # Débit en Mbps
        }

        
        try:
            result = subprocess.run(["iw", "dev", self.interface, "station", "dump"], capture_output=True, text=True)
            if result.returncode == 0:
                for line in result.stdout.split("\n"):
                    # Cherche le RSSI (Signal Level)
                    match_rssi = re.search(r"signal:\s+(-?\d+)", line)
                    if match_rssi:
                        metrics["RSSI"] = int(match_rssi.group(1))

                    # Cherche le débit
                    match_bitrate = re.search(r"rx bitrate:\s+([\d.]+)", line)
                    if match_bitrate:
                        metrics["Débit"] = float(match_bitrate.group(1))
        except Exception as e:
            print("Erreur lors de l'exécution de iw dev :", e)

        # 2️⃣ Récupérer le SNR avec `/proc/net/wireless`
        try:
            result = subprocess.run(["cat", "/proc/net/wireless"], capture_output=True, text=True)
            if result.returncode == 0:
                for line in result.stdout.split("\n"):
                    if self.interface in line:
                        values = line.split()
                        signal_level = float(values[2])  # RSSI en dBm
                        noise_level = float(values[3])  # Niveau de bruit en dBm
                        metrics["SNR"] = signal_level - noise_level  # Calcul du SNR
        except Exception as e:
            print("Erreur lors de l'exécution de /proc/net/wireless :", e)

        return metrics
