#!/bin/bash

# --Configuration--
PROJECT_ID="western-watch-418016"
COMPOSER_BUCKET="gs://europe-west1-pypi-airflow-3f26eac0-bucket"
DAGS_FOLDER="dags/"
BQ_DATASET="pypi_views"

echo "Début du déploiement..."

echo "Déploiement du DAG sur Cloud Composer"
gcloud storage cp dags/dag_pypi.py $COMPOSER_BUCKET/$DAGS_FOLDER


echo "Déploiement du code source sur Cloud Storage"
gcloud storage cp -r src/ $COMPOSER_BUCKET/data/
gcloud storage cp config/gcp_credentials.json $COMPOSER_BUCKET/data/config/

echo "Création ou mise à jour des vues BigQuery"
bq query --use_legacy_sql=false --location=US "
CREATE OR REPLACE VIEW \`${PROJECT_ID}.${BQ_DATASET}.downloads_by_day_country\` AS
SELECT 
    DATE(timestamp) AS download_date,
    country_code,
    file.project AS project_name,
    COUNT(*) AS total_downloads
FROM \`bigquery-public-data.pypi.file_downloads\`
GROUP BY download_date, country_code, project_name
ORDER BY download_date DESC;"

bq query --use_legacy_sql=false --location=US "
CREATE OR REPLACE VIEW \`${PROJECT_ID}.${BQ_DATASET}.download_intervals\` AS
SELECT 
    timestamp,
    country_code,
    file.project AS project_name,
    file.version AS project_version,
    file.filename AS file_name,
    timestamp - LAG(timestamp) OVER (
        PARTITION BY file.project 
        ORDER BY timestamp
    ) AS time_since_last_download,
    IF(file.filename LIKE '%.gz', TRUE, FALSE) AS is_gzipped
FROM \`bigquery-public-data.pypi.file_downloads\`;"

export GOOGLE_APPLICATION_CREDENTIALS="/home/airflow/gcs/data/config/gcp_credentials.json"
python src/main.py

echo "Déploiement terminé avec succès !"
