# Utiliser l'image de base Ubuntu 24.04

FROM ubuntu:24.04

# Mettre à jour les paquets et installer sudo

RUN apt-get update -y && apt-get install -y sudo

# Créer un utilisateur nommé "student" avec un mot de passe

RUN useradd -m -s /bin/bash student && echo "student:password" | chpasswd

# Ajouter l'utilisateur au groupe sudo pour qu'il 
# puisse utiliser sudo si nécessaire

RUN usermod -aG sudo student

# Définir l'utilisateur par défaut pour le conteneur

USER student

# Définir le répertoire de travail par défaut

WORKDIR /home/student