# DevOps & MLOps Pipeline: AWS Student Project

![CI Pipeline](https://github.com/Derbyneon/devops-mlops-aws-student-project/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.9-blue.svg)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue.svg)
![AWS](https://img.shields.io/badge/AWS-EC2-orange.svg)

## 📋 Contexte du Projet

Ce projet s'inscrit dans le cadre d'un module académique visant à implémenter un pipeline complet **DevOps et MLOps**. L'objectif est d'automatiser le cycle de vie d'une application de Machine Learning, de l'entraînement du modèle jusqu'à son déploiement conteneurisé sur le Cloud AWS.

**Objectifs principaux :**
1.  **MLOps** : Entraînement, sérialisation et versioning d'un modèle de classification (Iris Dataset).
2.  **DevOps** : Conteneurisation de l'application via Docker.
3.  **CI/CD** : Automatisation des tests et de l'intégration via GitHub Actions.
4.  **Cloud** : Déploiement sur une instance AWS EC2.

---

## 🏗 Architecture & Workflow

Le pipeline suit les étapes suivantes :
1.  **Data & Training** : Préparation des données et entraînement d'un `RandomForestClassifier` (Notebook/Script).
2.  **Serialization** : Export du modèle entraîné sous format `model.pkl`.
3.  **API Serving** : Exposition du modèle via une API REST Flask (`/predict`).
4.  **Containerization** : Construction d'une image Docker optimisée.
5.  **Continuous Integration** : Tests unitaires automatiques à chaque `push` sur GitHub.
6.  **Deployment** : Exécution du conteneur sur AWS EC2.

---

## 📂 Structure du Projet

L'organisation du dépôt respecte les standards industriels :

```text
devops-mlops-aws-student-project/
├── .github/
│   └── workflows/
│       └── ci.yml          # Workflow GitHub Actions (CI)
├── api/
│   ├── __init__.py
│   ├── app.py              # Application Flask (Point d'entrée)
│   └── model_loader.py     # Logique de chargement du modèle
├── docker/
│   └── Dockerfile          # Configuration de l'image Docker
├── docs/                   # Documentation et Captures d'écran
│   ├── architecture.png
│   └── screenshots/
├── model/
│   └── model.pkl           # Modèle sérialisé (généré après entraînement)
├── notebooks/
│   └── train_model.ipynb   # Notebook d'entraînement (Data Science)
├── tests/
│   └── test_api.py         # Tests unitaires (Pytest)
├── .gitignore
├── README.md
└── requirements.txt        # Dépendances Python