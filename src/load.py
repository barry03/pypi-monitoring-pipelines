import os
from google.cloud import storage
import config

def upload_to_gcs(local_file_path, bucket_name, destination_blob_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    
    blob.upload_from_filename(local_file_path)
    print(f"Fichier {local_file_path} uploadé sur GCS sous {destination_blob_name}")
    

def save_data(df, bucket_name):
    """Sauvegarde les données localement et les upload sur Google Cloud Storage (GCS)."""
    local_file_path = "data/pypi_downloads.csv"
    gcs_file_path = "data/pypi_downloads.csv"

    # Création du dossier en local s'il n'éxiste pas
    os.makedirs("data", exist_ok=True)

    df.to_csv(local_file_path, index=False)

    if "AIRFLOW_HOME" in os.environ:
        print("Détection d'éxécution via Airflow")
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(gcs_file_path)
        blob.upload_from_filename(local_file_path)
        print(f"Fichier uploadé sur GCS : gs://{bucket_name}/{gcs_file_path}")
    else:
        print("Exécution locale détectée.")