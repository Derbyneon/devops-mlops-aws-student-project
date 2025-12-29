# Image de base légère
FROM python:3.9-slim

# Définition du répertoire de travail
WORKDIR /app

# Copie des dépendances en premier pour optimiser le cache Docker
COPY requirements.txt .

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copie de tout le projet (code + modèle)
COPY . .

# Variable d'environnement pour Flask
ENV FLASK_APP=api/app.py

# Exposition du port
EXPOSE 5000

# Commande de démarrage (lancement module python pour gérer les imports relatifs)
CMD ["python", "-m", "api.app"]