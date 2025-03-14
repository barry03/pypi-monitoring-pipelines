import streamlit as st
import utils
import config
import matplotlib.pyplot as plt

# Configuration de la page Streamlit
st.set_page_config(page_title="Dashboard PyPi", layout="wide")

# Réduction de la taille par défaut des graphiques
plt.rcParams['figure.figsize'] = [7, 3]
# Chargement des données et prétraitement
df = utils.load_data()
df = utils.preprocess_timestamps(df)

# indicateurs principaux
metrics = utils.metrics(df)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Nombre total de téléchargements", metrics["total_downloads"])
col2.metric("Taille totale des fichiers téléchargés (MB)", metrics["total_size_mb"])
col3.metric("Nombre de projets PyPi uniques", metrics["unique_projects"])
col4.metric("Nombre de versions uniques", metrics["unique_versions"])

# Affichage des graphiques
st.subheader("Téléchargements par pays")
st.pyplot(utils.plot_downloads_by_country(df))

st.subheader("Top Projets PyPi les plus téléchargés")
st.pyplot(utils.plot_top_projects(df))

st.subheader("Téléchargements par jour de la semaine")
st.pyplot(utils.plot_downloads_by_day(df))

st.subheader("Nombre moyen de téléchargements par heure")
st.pyplot(utils.plot_downloads_by_hour(df))

st.write("Dashboard interactif créé avec Streamlit !")