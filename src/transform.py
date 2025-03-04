import pandas as pd

def transform_data(df):
    # Gestion des conversions
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df.dropna(subset=["timestamp"], inplace=True)

    df["day_of_week"] = df["timestamp"].dt.day_name()
    df["hour"] = df["timestamp"].dt.hour
    df["is_gzipped"] = df["filename"].str.endswith(".gz")

    return df