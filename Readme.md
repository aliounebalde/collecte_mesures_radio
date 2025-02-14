# Collecte automatisés de mesures Radio
Ceci est un projet qui consiste à automatiser la collecte automatique de mesures radio. Les tests seront effectués sur les technologies WIFI IEE 802.11 et/ ou LTE. En effet, nous voulons dans une périmètre géographique relevés des mesures tels que le niveau de puissance reçue, le débit, le taux de SNR, même la latence en fonction de la distance, de l'environnement (outdoor, indoor). La finalité sera qu'à la fin qu'on puisse faire des études de performances en fonction de ses résultats.
---

## Objectif du projet

L'objectif de ce projet est de collecter des données WiFi (RSSI, SNR, débit) à intervalles réguliers, de les timestamper, et de les sauvegarder dans un fichier JSON. Ces données peuvent ensuite être utilisées pour analyser les performances du réseau WiFi en fonction du temps et de la position géographique.
---

## Fonctionnalités

- **Collecte des métriques WiFi** : RSSI, SNR, débit.
- **Timestamp des mesures** : Chaque mesure est associée à un timestamp précis.
- **Sauvegarde des données** : Les données sont sauvegardées dans un fichier JSON structuré.
- **Gestion des erreurs** : Logging des erreurs pour faciliter le débogage.
- **Configuration facile** : Utilisation d'un fichier `config.json` pour paramétrer le projet.

## Utilisation

Pour lancer la collecte, exécutez le script main.py

```bash
python main.py
```

### Résultat attendu

- Un dossier results sera créé (s'il n'existe pas déjà).

- Un fichier JSON contenant les mesures sera généré dans ce dossier, avec un nom basé sur la date et l'heure de la collecte (ex: results_2023-10-15_14-30-00.json).

