import json
import os
import xml.etree.ElementTree as ET
from math import radians, sin, cos, sqrt, atan2
import datetime
import main as M
def haversine(lat1, lon1, lat2, lon2):
    """
    Calcule la distance entre deux points GPS en utilisant la formule de Haversine.
    :param lat1: Latitude du premier point.
    :param lon1: Longitude du premier point.
    :param lat2: Latitude du deuxième point.
    :param lon2: Longitude du deuxième point.
    :return: Distance en mètres.
    """
    R = 6371000  # Rayon de la Terre en mètres
    phi1, phi2 = radians(lat1), radians(lat2)
    delta_phi = radians(lat2 - lat1)
    delta_lambda = radians(lon2 - lon1)
    a = sin(delta_phi / 2)**2 + cos(phi1) * cos(phi2) * sin(delta_lambda / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

def read_gps_txt(file_path):
    """
    Lit un fichier GPS au format .txt et retourne une liste de points GPS.
    :param file_path: Chemin du fichier .txt.
    :return: Liste de dictionnaires contenant latitude, longitude et timestamp.
    
    """
    points = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        headers = lines[0].strip().split(',')
        for line in lines[1:]:
            values = line.strip().split(',')
            point = {
                "latitude": float(values[headers.index("latitude")]),
                "longitude": float(values[headers.index("longitude")]),
                "timestamp": values[headers.index("date time")]
            }
            points.append(point)
    return points
def read_gps_gpx(file_path):
    """
    Lit un fichier GPS au format .gpx et retourne une liste de points GPS.
    :param file_path: Chemin du fichier .gpx.
    :return: Liste de dictionnaires contenant latitude, longitude et timestamp.
    """
    points = []
    tree = ET.parse(file_path)
    root = tree.getroot()
    namespace = {'gpx': 'http://www.topografix.com/GPX/1/0'}
    for wpt in root.findall('.//gpx:wpt', namespace):
        lat = float(wpt.attrib['lat'])
        lon = float(wpt.attrib['lon'])
        time = wpt.find('gpx:time', namespace).text
        points.append({
            "latitude": lat,
            "longitude": lon,
            "timestamp": time
        })
    return points

def generate_json_output(points, ap_lat,ap_lon, output_file):
    """
    Génère un fichier JSON contenant la distance et le timestamp pour chaque point GPS.
    :param points: Liste de points GPS.
    :param ap_lat: Latitude du point d'accès (AP).
    :param ap_lon: Longitude du point d'accès (AP).
    :param output_file: Chemin du fichier JSON de sortie.
    
    """

    results = []
    for point in points:
        distance = haversine(ap_lat,ap_lon,point['latitude'],point['longitude'])
        results.append({
            'timestamp': point['timestamp'],
            'distance_m' : distance
        })
    
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=4)
    
def main(input_file):
    """
    Point d'entrée principal du programme.
    :param input_file: Chemin du fichier d'entrée (.txt ou .gpx).
    :param output_file: Chemin du fichier JSON de sortie.
    """

    if input_file.endswith('.txt'):
        points = read_gps_txt(input_file)
    elif input_file.endswith('.gpx'):
        points = read_gps_gpx(input_file)
    else:
        raise ValueError("Format de fichier non supporté. Utilisez .txt ou .gpx.")

    # Le point d'accès (AP) est le premier point du fichier
    ap_lat = points[0]["latitude"]
    ap_lon = points[0]["longitude"]
    
    # charger le fichier de configuration
    config = M.load_config()
    
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    output_file = os.path.join(config["output_dir"],f'distance_{current_date}.json')
    # Générer le fichier JSON
    generate_json_output(points, ap_lat, ap_lon, output_file)
    print(f"Fichier JSON généré avec succès : {output_file}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python gps_processor.py <input_file>")
    else:
        main(sys.argv[1])