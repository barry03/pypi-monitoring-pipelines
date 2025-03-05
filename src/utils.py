import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Fonction de chargement des données
@st.cache_data
def load_data(filepath="data/pypi_downloads.csv"):
    df = pd.read_csv(filepath)
    return df

# Fonction pour nettoyer et convertir le timestamp
def preprocess_timestamps(df):
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df["day_of_week"] = df["timestamp"].dt.day_name()
    df["day_of_week"] = pd.Categorical(df["day_of_week"], 
                                   categories=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                                   ordered=True)
    df["hour"] = df["timestamp"].dt.hour
    return df

# Fonction pour obtenir les métriques principales
def metrics(df):
    """Calcule les métriques principales."""
    total_downloads = df.shape[0]
    total_size_mb = round(df["package_size"].sum() / 1e6, 2)
    unique_projects = df["project"].nunique()
    unique_versions = df["version"].nunique()
    
    return {
        "total_downloads": total_downloads,
        "total_size_mb": total_size_mb,
        "unique_projects": unique_projects,
        "unique_versions": unique_versions
    }

# Fonction pour créer un graphique des téléchargements par pays
def plot_downloads_by_country(df):
    """Affichage du graphique des téléchargements par pays."""
    fig, ax = plt.subplots()
    top_countries = df["country_code"].value_counts().head(10)
    sns.barplot(x=top_countries.values, y=top_countries.index, ax=ax)
    ax.set_xlabel("Nombre de téléchargements")
    ax.set_ylabel("Pays")
    return fig

# Fonction pour créer un graphique des projets les plus téléchargés
def plot_top_projects(df):
    """Affichage du graphique des projets PyPi les plus téléchargés."""
    fig, ax = plt.subplots()
    top_projects = df["project"].value_counts().head(10)
    sns.barplot(x=top_projects.values, y=top_projects.index, ax=ax)
    ax.set_xlabel("Nombre de téléchargements")
    ax.set_ylabel("Projet")
    return fig

# Fonction pour créer un graphique des téléchargements par jour de la semaine
def plot_downloads_by_day(df):
    fig, ax = plt.subplots()
    downloads_per_day = df.groupby("day_of_week", observed=False).size()
    sns.barplot(x=downloads_per_day.index, y=downloads_per_day.values, ax=ax)
    ax.set_xlabel("Jour de la semaine")
    ax.set_ylabel("Nombre de téléchargements")
    return fig

# Fonction pour afficher le nombre moyen de téléchargements par heure
def plot_downloads_by_hour(df):
    fig, ax = plt.subplots()
    downloads_per_hour = df.groupby("hour").size().reindex(range(24), fill_value=0)
    sns.lineplot(x=downloads_per_hour.index, y=downloads_per_hour.values, ax=ax, marker="o")
    ax.set_xlabel("Heure")
    ax.set_ylabel("Nombre moyen de téléchargements")
    return fig
