import os

if os.path.exists("/home/airflow/gcs/data/config/gcp_credentials.json"):
    GCP_CREDENTIALS_PATH = "/home/airflow/gcs/data/config/gcp_credentials.json"
else:
    GCP_CREDENTIALS_PATH = "config/gcp_credentials.json"

GCP_PROJECT_ID = "western-watch-418016"

# Chemin des fichiers de données
DATA_PATH = "data/"

# Nom des tables BigQuery utilisées
BQ_TABLE_DOWNLOADS = "bigquery-public-data.pypi.file_downloads"
BQ_TABLE_METADATA = "bigquery-public-data.pypi.distribution_metadata"

GCS_BUCKET_NAME = "europe-west1-pypi-airflow-3f26eac0-bucket"

# Nombre de lignes à récupérer
BQ_LIMIT = 10000000
#DAYS_HISTORY = 15

# Format du fichier de sortie
DATA_FORMAT = "csv"
