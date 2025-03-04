import os
import sys
from src import config

print(f"TEST CHEMIN : GCP_CREDENTIALS_PATH = {config.GCP_CREDENTIALS_PATH}")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = config.GCP_CREDENTIALS_PATH

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.extract import get_data
from src.transform import transform_data
from src.load import save_data

if __name__ == "__main__":
    print("Extraction des données depuis BigQuery")
    df = get_data()

    print("Transformation des données")
    df = transform_data(df)

    print("Sauvegarde des données")
    save_data(df, config.GCS_BUCKET_NAME)

    print("Processus terminé avec succès !")