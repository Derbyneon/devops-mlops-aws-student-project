from flask import Flask, request, jsonify
from api.model_loader import load_model
import numpy as np
import logging

# Configuration des logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Chargement du modèle au démarrage
try:
    model = load_model()
    logger.info("Modèle chargé avec succès.")
except Exception as e:
    logger.error(f"Erreur lors du chargement du modèle : {e}")
    model = None

@app.route('/')
def home():
    return jsonify({"message": "API ML opérationnelle. Utilisez l'endpoint /predict POST."})

@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return jsonify({"error": "Modèle non disponible"}), 500

    try:
        data = request.get_json()
        
        # Validation basique des données
        if 'features' not in data:
            return jsonify({"error": "Le champ 'features' est requis"}), 400
            
        features = np.array(data['features']).reshape(1, -1)
        
        # Prédiction
        prediction = model.predict(features)
        
        return jsonify({
            "prediction": int(prediction[0]),
            "status": "success"
        })

    except Exception as e:
        logger.error(f"Erreur de prédiction : {str(e)}")
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    # Écoute sur toutes les interfaces pour Docker/AWS
    app.run(host='0.0.0.0', port=5000)