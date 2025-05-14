# Docker Evaluation

Ce repository contient plusieurs travaux pratiques (TP) liés à Docker, couvrant différents concepts tels que les volumes, les multi-services, la sécurité, le déploiement, et bien plus encore.

## Structure du projet

### TP1 corrigé par en classe par Alex (Notre formateur devops)

- **Dockerfile** : Crée une image Ubuntu avec un utilisateur non-root nommé `student` et des privilèges sudo.

### TP2 Multi-stage

- **Dockerfile** : Implémente un build multi-stage avec Node.js pour construire une application web et Nginx pour servir les fichiers statiques.
- **package.json** : Contient les scripts et dépendances pour l'application Node.js.
- **src/** : Contient les fichiers source de l'application web.
  - `index.html` : Page HTML principale.
  - `style.css` : Styles CSS pour la page.
  - `app.js` : Script JavaScript pour la logique de l'application.

### TP3 Volumes

- **Dockerfile** : Configure une application Flask.
- **docker-compose.yml** : Définit les volumes pour la persistance des données, des logs, et des configurations.
- **app.py** : Application Flask qui lit et écrit dans les volumes.
- **config/settings.conf** : Fichier de configuration utilisé par l'application.

### TP5 flask-docker

- **docker-compose.yml** : Configure un service Flask (backend) et un serveur Nginx pour le proxy inverse.
- **backend/** : Contient l'application Flask.
  - `app.py` : Application Flask qui rend une page HTML.
  - `templates/index.html` : Page HTML rendue par Flask.
  - `dockerfile` : Dockerfile pour construire l'image Flask.
- **nginx/default.conf** : Configuration Nginx pour rediriger les requêtes vers le backend.

### TP6 Multi-services

- **dockerfile** : Dockerfile pour une application Flask.
- **docker-compose.yml** : Définit un service Flask avec des variables d'environnement et des volumes.
- **docker-compose.override.yml** : Configuration pour le mode développement.
- **docker-compose.prod.yml** : Configuration pour le mode production.
- **.env** : Variables d'environnement pour le développement.
- **.env.development** : Variables d'environnement spécifiques au développement.
- **.env.production** : Variables d'environnement spécifiques à la production.
- **app/app.py** : Application Flask.

### TP9 Sécurité

- **Dockerfile** : Configure une application Flask avec un utilisateur non-root pour des raisons de sécurité.
- **docker-compose.yml** : Définit les limites de ressources pour le conteneur.
- **src/app.py** : Application Flask simple.
- **requirements.txt** : Dépendances Python.

### TP10 Déploiement

- **Dockerfile** : Dockerfile pour une application Flask.
- **docker-compose.yml** : Configure un déploiement avec plusieurs réplicas, secrets, et volumes.
- **app.py** : Application Flask.
- **requirements.txt** : Dépendances Python.

## Comment utiliser ce repository

1. Clonez le repository :
   ```bash
   git clone <url-du-repository>
   cd Docker-eval
   ```
