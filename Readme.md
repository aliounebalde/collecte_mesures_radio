# Collecte automatisés de mesures Radio
Ceci est un projet qui consiste à automatiser la collecte automatique de mesures radio. Les tests seront effectués sur les technologies WIFI IEE 802.11 et/ ou LTE. En effet, nous voulons dans une périmètre géographique relevés des mesures tels que le niveau de puissance reçue, le débit, le taux de SNR, même la latence en fonction de la distance, de l'environnement (outdoor, indoor). La finalité sera qu'à la fin qu'on puisse faire des études de performances en fonction de ses résultats.
---

## Table des matières

1. [Objectif du projet](#objectif-du-projet)
2. [Fonctionnalités](#fonctionnalités)
3. [Prérequis](#prérequis)
4. [Installation](#installation)
5. [Utilisation](#utilisation)
6. [Structure du projet](#structure-du-projet)
7. [Configuration](#configuration)
8. [Combinaison des fichiers JSON](#combinaison-des-fichiers-json)
9. [Tests](#tests)

--- 

## Objectif du projet

L'objectif de ce projet est de :
- Collecter des données WiFi (RSSI, SNR, débit) à intervalles réguliers.
- Collecter des données GPS (latitude, longitude, timestamp) en même temps.
- Calculer la distance entre chaque point GPS et le point d'accès (AP).
- Combiner les mesures WiFi et les distances GPS en fonction du timestamp.
- Générer un fichier JSON structuré pour l'analyse des performances réseau.

---

## Fonctionnalités

- **Collecte des métriques WiFi** : RSSI, SNR, débit.
- **Collecte des données GPS** : Latitude, longitude, timestamp.
- **Calcul de la distance** : Utilisation de la formule de Haversine pour calculer la distance entre chaque point GPS et l'AP.
- **Combinaison des données** : Fusion des mesures WiFi et des distances GPS en fonction du timestamp.
- **Sauvegarde des données** : Les données sont sauvegardées dans un fichier JSON structuré.
- **Gestion des erreurs** : Logging des erreurs pour faciliter le débogage.
- **Configuration facile** : Utilisation d'un fichier `config.json` pour paramétrer le projet.

---

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre système :

- **Python**
- **Outils système** : `iw`, `cat` (disponibles sur la plupart des distributions Linux).

---

## Installation

Clonez ce dépôt sur votre machine locale :
   ```bash
   git clone https://github.com/votre-utilisateur/votre-projet.git
   cd votre-projet
   ```

--- 

## Utilisation

1. Pour lancer la collecte, exécutez le script main.py

    ```bash
    python main.py
    ```
2. Pour calculer la distance en fonction des coordonnées GPS 

    Nous utilisons une application mobile (**Gps Logger**) pour collecter les coordonnées Lat, Lon et générer ainsi un fichier .txt et/ou .gpx que nous utiliserons pour estimer la distance à partir de la formule de Haversine

    ```bash
    python gps_processor.py <input_file>
    ```
3. Combinaison 
    
    ```bash
    python combine_measurements.py wifi_measurements.json gps_distances.json
    ```

---

## Structures du projet

📁 collecte_mesures_radio
│── 📄 main.py        # Script pour collecter les mesures
│── 📄 plot_moy2.py           # Script d'analyse et de visualisation
│── 📄 gps_processor.py          # Script de calcul de distance en fonction des données gps
│── 📄 combine_measurements.py           # Script combinant distance ,mesures en fonction de timestamp
│── 📁 gps_data         #  contient les données gps recueillis à partir de GPS logger
│── 📁 results         #  contient tous les resultats de notre projets
&nbsp;&nbsp;&nbsp;&nbsp;│── 📁 wifi          # dossier de fichiers JSON contenant les mesures collectées
&nbsp;&nbsp;&nbsp;&nbsp;|── 📁 distances          # dossier de fichiers JSON contenant les distances
&nbsp;&nbsp;&nbsp;&nbsp;│── 📁 final          # dossier de fichiers JSON contenant les resultats final
│── 📄 config.json             # fichier de configuration du projet
│── 📄 README.md              # Documentation du projet

---
## Résultat attendu

- Un dossier results sera créé (s'il n'existe pas déjà).

- Un fichier JSON contenant les mesures sera généré dans ce dossier, avec un nom basé sur la date et l'heure de la collecte (ex: wifi_measurements_2023-10-15_14-30-00.json).

- Un fichier json contenant les distances et le timestamp

- Et enfin le fichier final qui combine les deux

---

# Auteurs

**Alioune BALDE** https://github.com/aliounebalde/
**Mohamed Bouhlassi**


