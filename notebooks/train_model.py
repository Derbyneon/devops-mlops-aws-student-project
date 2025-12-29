import pandas as pd
import numpy as np
import joblib
import os
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# --- CONFIGURATION ---
# On se base sur le fait qu'on exécute le script depuis le dossier 'notebooks'
# Le dossier model doit être au même niveau que notebooks
MODEL_DIR = "../model"
MODEL_PATH = os.path.join(MODEL_DIR, "model.pkl")

# Création du dossier si inexistant
os.makedirs(MODEL_DIR, exist_ok=True)

print(">>> 1. Environnement prêt. Chargement des données...")

# --- CHARGEMENT & SPLIT ---
iris = load_iris()
X = iris.data
y = iris.target

# 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- ENTRAÎNEMENT ---
print(">>> 2. Entraînement du modèle (Random Forest)...")
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# --- ÉVALUATION ---
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"\n--------------------------------")
print(f"Accuracy du modèle : {accuracy:.4f}")
print(f"--------------------------------\n")
print("Rapport de classification :")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# --- SAUVEGARDE ---
print(">>> 3. Sauvegarde du modèle...")
joblib.dump(clf, MODEL_PATH)

if os.path.exists(MODEL_PATH):
    print(f"SUCCESS: Modèle sauvegardé avec succès dans : {os.path.abspath(MODEL_PATH)}")
else:
    print("ERROR: Échec de la sauvegarde.")