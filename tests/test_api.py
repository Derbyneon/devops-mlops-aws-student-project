import pytest
import json
from api.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test de la route racine"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"API ML" in rv.data

def test_predict(client):
    """Test de la prédiction avec des données valides (Iris data)"""
    payload = {"features": [5.1, 3.5, 1.4, 0.2]}
    rv = client.post('/predict', 
                     data=json.dumps(payload), 
                     content_type='application/json')
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert "prediction" in json_data