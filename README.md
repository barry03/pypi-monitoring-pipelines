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

Voici un aperçu de l'architecture du pipeline ETL :

<img src="docs/arch.png" alt="Architecture ETL PyPi" width="400">

## **Installation et Configuration**
### 1 **Prérequis**
Assurez-vous d'avoir :
- **Python 3.11+** et `pip` installés
- **Google Cloud SDK** (`gcloud`) configuré avec un projet actif
- **BigQuery API, Cloud Storage API et Cloud Composer activés**
- **Un bucket GCS** pour stocker les fichiers transformés
- **Un environnement Cloud Composer (Airflow)** configuré

### 2 **Cloner le projet et installer les dépendances**
```bash
git clone https://github.com/votre-repo/pypi_project.git
cd pypi_project
pip install -r requirements.txt



