from google.cloud import bigquery
import pandas as pd
from src import config

def get_data():
    client = bigquery.Client(project=config.GCP_PROJECT_ID)

    query = """
    SELECT 
        f.timestamp,
        f.country_code,
        f.file.project AS project,
        f.file.version AS version,
        d.size AS package_size,
        f.file.type AS file_type
    FROM `bigquery-public-data.pypi.file_downloads` f
    JOIN `bigquery-public-data.pypi.distribution_metadata` d
    ON f.file.project = d.name
    AND f.file.version = d.version
    WHERE f.timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 15 DAY)
    LIMIT 1000000
    """

    df = client.query(query).to_dataframe()
    return df