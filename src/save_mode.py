"""
Persist the trained model pipeline for inference and deployment.
"""

import mlflow
import mlflow.sklearn
import joblib
from pathlib import Path

# Ensure correct MLflow tracking server
mlflow.set_tracking_uri("http://127.0.0.1:5000")

# Load latest registered model
model_uri = "models:/HeartDiseaseClassifier/latest"
model = mlflow.sklearn.load_model(model_uri)

# Resolve path relative to this script
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "heart_disease_model.pkl"

# Save model
joblib.dump(model, MODEL_PATH)

print(f"Model saved successfully at: {MODEL_PATH}")
