# Utiliser une image Python légère
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt
COPY requirements.txt requirements.txt

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application dans le conteneur
COPY . .

# Exposer le port 5001 pour le service stock
EXPOSE 5001

# Commande pour démarrer l'application
CMD ["python", "app.py"]
