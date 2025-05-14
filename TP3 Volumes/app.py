from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    # Lire un fichier de configuration
    config_path = "/app/config/settings.conf"
    config_content = "Configuration introuvable."
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            config_content = f.read()

    # Créer un fichier dans le volume de données
    data_path = "/app/data/example.txt"
    with open(data_path, "w") as f:
        f.write("Ceci est un fichier de données persistantes.\n")

    # Écrire un log
    log_path = "/app/logs/app.log"
    with open(log_path, "a") as f:
        f.write("L'application a démarré.\n")

    return f"""
    <h1>Bienvenue sur votre application Flask</h1>
    <p>Configuration en cours... :</p>
    
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)