import joblib
import os

def load_model():
    """
    Charge le modèle sérialisé depuis le chemin spécifié.
    Gère les erreurs si le modèle est introuvable.
    """
    model_path = os.path.join(os.path.dirname(__file__), '../model/model.pkl')
    
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Le modèle n'a pas été trouvé au chemin : {model_path}")
        
    print(f"Chargement du modèle depuis : {model_path}")
    return joblib.load(model_path)