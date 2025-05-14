# Utilisation d'une image de base
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY . /app

# Installer Flask
RUN pip install flask

# Commande pour exécuter l'application
CMD ["python", "app.py"]