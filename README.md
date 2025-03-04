# Pipeline de Monitoring des Téléchargements PyPi

## Présentation

Ce projet met en place un pipeline ETL pour monitorer les téléchargements PyPi sur BigQuery. Il comprend :
- **Extraction** des données depuis `bigquery-public-data.pypi.file_downloads`
- **Transformation** des données (formatage, ajout de métriques comme `is_gzipped`)
- **Chargement** des données sur **Google Cloud Storage (GCS)**
- **Orchestration** du pipeline avec **Airflow (Cloud Composer)**
- **Visualisation** avec **Looker Studio et Streamlit**
- **Création de vues BigQuery** pour des analyses optimisées

## **Architecture du projet**



