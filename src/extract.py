from google.cloud import bigquery
import pandas as pd
from src import config

def get_data():
    client = bigquery.Client(project=config.GCP_PROJECT_ID)

    query = """
    WITH filtered_data AS (
        SELECT 
            timestamp,
            country_code,
            file.project AS project,
            file.version AS version,
            d.size AS package_size,
            file.type AS file_type,
            file.filename AS filename
        FROM `bigquery-public-data.pypi.file_downloads` f
        JOIN `bigquery-public-data.pypi.distribution_metadata` d
        ON f.file.project = d.name
        AND f.file.version = d.version
        WHERE timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 15 DAY)
        LIMIT {}
    )
    SELECT * FROM filtered_data
    ORDER BY timestamp DESC
    """.format(config.BQ_LIMIT)
    
    df = client.query(query).to_dataframe()
    return df