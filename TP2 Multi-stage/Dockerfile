# ------------ STAGE 1 : Build avec Node.js ------------ 
FROM node:18-alpine AS build

# Définir le répertoire de travail
WORKDIR /app


COPY package*.json ./

# Installer les dépendances
RUN npm install

# Copier le reste des fichiers de l'application
COPY . .

# Lancer la commande de build
RUN npm run build

# ------------ STAGE 2 : Serveur NGINX ------------ 
FROM nginx:alpine

# Supprimer les fichiers par défaut de Nginx
RUN rm -rf /usr/share/nginx/html/*

# Copier les fichiers générés par le build 
COPY --from=build /app/dist /usr/share/nginx/html

# Exposer le port 80 pour accéder à l'application
EXPOSE 80


CMD ["nginx", "-g", "daemon off;"]