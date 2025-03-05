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

Voici un aperçu de l'architecture du pipeline ETL : Le pipeline suit une architecture en plusieurs étapes allant de l’extraction des données brutes jusqu'à leur visualisation dans des dashboards interactifs.

<img src="docs/archi.png" alt="Architecture ETL PyPi" width="600" heigth="450">

## **Installation et Configuration**
### 1 - **Prérequis**
Assurez-vous d'avoir :
- **Python 3.11+** et `pip` installés
- **Google Cloud SDK** (`gcloud`) configuré avec un projet actif
- **BigQuery API, Cloud Storage API et Cloud Composer activés**
- **Un bucket GCS** pour stocker les fichiers transformés
- **Un environnement Cloud Composer (Airflow)** configuré

### **2 - Cloner le projet et installer les dépendances**
```bash
git clone https://github.com/votre-repo/pypi_project.git
cd pypi_project
pip install -r requirements.txt
```
### **3 - Déploiement**
Ce projet peut être déployé de deux manières : 1. Avec le script `deploy.sh` (déploiement automatiquement sur GCS & BigQuery)
2. **Avec Docker** (sous forme d'image conteneurisée)

**Option 1:** Déploiement Automatisé avec `deploy.sh`
Ce script automatise tout le processus:
- Envoi du code source dans GCS
- Déploiement du DAG sur Cloud Composer
- Création/Mise à jour des vues BigQuery
- Lancement du pipeline en local
```bash
chmod +x deploy.sh  # Rendre le script exécutable
./deploy.sh
```
NB: Assurez-vous d’avoir configuré `gcloud` et d’être connecté à votre projet GCP avant d’exécuter ce script.

**Option 2 :** Déploiement avec Docker
Une image Docker a été créée pour éxécuter ce projet dans un environnement conteneurisé.

**Étapes de déploiement :**
1. Construire l'image Docker:
```bash
docker build -t pypi-monitoring-pipeline .
```
2. Exécuter le conteneur et lancer le pipeline :
```bash
docker run --rm pypi-monitoring-pipeline
```
3. Pousser l’image sur Google Container Registry (GCR) :
```bash
gcloud auth configure-docker
docker tag pypi-monitoring-pipeline gcr.io/<PROJECT_ID>/pypi-monitoring-pipeline
docker push gcr.io/<PROJECT_ID>/pypi-monitoring-pipeline
```
**NB:** Remplacer <PROJECT_ID> par l'ID de votre projet

**Déploiement du DAG Airflow (Manuel)**
Si vous souhaitez ajouter ou mettre à jour manuellement le DAG sur Cloud Composer :
```bash
gcloud storage cp dags/dag_pypi.py gs://<YOUR_COMPOSER_BUCKET>/dags/
```
- Accédez à Airflow Web UI depuis Cloud Composer.
- Activez le DAG pypi_data_pipeline
- Lancez une exécution manuelle.

### **4 - Exécution du pipeline en local**
  ```bash
  python src/main.py
  ```

### **5 - Utilisation des Vues BigQuery**
Ce projet utilise les tables brutes **BigQuery Public Datasets**, mais pour améliorer les performances, des **vues BigQuery** sont disponibles.

**- Pourquoi utiliser les vues BigQuery ?**

- **Moins de volume de données extraites** → Réduction des coûts et des temps d’exécution.
- **Données déjà filtrées et pré-transformées** → Moins de transformations dans le pipeline.
- **Plus rapide pour l'analyse et le dashboard**.

**- Vues disponibles :**
| Nom de la vue | Description |
| ------ | ------ |
| `pypi_views.fifth_downloads` | Contient uniquement les téléchargements des `15 derniers jours`|
| `pypi_views.downloads_by_day_country`   | Agrège le nombre de téléchargements par jour et par pays|
| `pypi_views.gzipped_downloads` | Filtre uniquement les fichiers compressés (`.gz`)|
| `pypi_views.download_intervals` | Analyser la fréquence des téléchargements des projets sur PyPI|


**- Comment utiliser une vue dans le pipeline ?**
Si vous souhaitez utiliser une **vue BigQuery** au lieu des tables brutes, modifiez `extract.py` en remplaçant la requête SQL par :
```python
query = "SELECT * FROM `western-watch-418016.pypi_views.fifth_downloads`"
```

### **6 - Accès aux résultats**
- Les fichiers transformés sont disponibles sur **Cloud Storage** (gs://<YOUR_BUCKET_NAME>/data/)
- Les vues sont accessibles sur BigQuery (western-watch-418016.pypi_views).
- Les dashboards sont accessibles sur Looker Studio ou Streamlit.

### **7 - Visualisation des Dashboards**

Les dashboards sont accessibles via **Looker Studio** (via BigQuery) ou en local avec **Streamlit**.

** - Exécution du dashboard avec Streamlit**
Si vous souhaitez visualiser les données en local, exécutez :

```bash
streamlit run src/dashboard.py
```
- Prérequis : Assurez-vous d’avoir Streamlit installé dans votre environnement
```bash
pip install streamlit
```

### **8 - Contact**
Si vous avez des questions, vous pouvez me contacter :
- 📧 Email : barrydjoulde15@gmail.com
- 🔗 LinkedIn : https://www.linkedin.com/in/djould%C3%A9-barry-24868a187
- 📝 Issues : Ouvrez une issue sur [le repo GitLab](https://gitlab.com/barrydjoulde/pypi-monitoring-pipeline)





