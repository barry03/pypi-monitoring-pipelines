# Utilisation d'une image Python officielle
FROM python:3.11-slim

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Copie les fichiers du projet dans le conteneur
COPY src/ ./src/
COPY config/ ./config/
COPY config/requirements.txt .

# Installation des dépendances
RUN pip install --no-cache-dir -r config/requirements.txt

# Définir la variable d'environnement pour les credentials
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/config/gcp_credentials.json

# Définition du point d'entrée par défaut
CMD ["python", "src/main.py"]
