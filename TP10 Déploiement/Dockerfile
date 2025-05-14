# Utiliser une image de base Python officielle
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /usr/src/app

# Copier le fichier requirements.txt contenant les dépendances
COPY requirements.txt ./

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers de l'application
COPY . .

# Exposer le port sur lequel l'application s'exécute
EXPOSE 5000

# Commande pour démarrer l'application
CMD ["python", "app.py"]