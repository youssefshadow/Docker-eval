# Utiliser une image Python légère
FROM python:3.9-slim

# Créer un utilisateur non-root
RUN useradd -m nonrootuser
USER nonrootuser

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY --chown=nonrootuser:nonrootuser src/ /app/
COPY requirements.txt /app/

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port de l'application
EXPOSE 5000

# Commande de démarrage
CMD ["python", "app.py"]