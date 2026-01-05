"""
Inference script to load the trained model and make predictions.
"""

import joblib
import pandas as pd
from pathlib import Path

# Resolve model path relative to this file (robust across environments)
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "heart_disease_model.pkl"

# Load saved model
model = joblib.load(MODEL_PATH)

# Example input (single patient)
sample_input = pd.DataFrame([{
    "age": 55,
    "sex": 1,
    "cp": 2,
    "trestbps": 140,
    "chol": 250,
    "fbs": 0,
    "restecg": 1,
    "thalach": 150,
    "exang": 0,
    "oldpeak": 1.5,
    "slope": 2,
    "ca": 0,
    "thal": 3
}])

# Predict
prediction = model.predict(sample_input)
probability = model.predict_proba(sample_input)[0][1]

print(f"Prediction (0 = No disease, 1 = Disease): {prediction[0]}")
print(f"Confidence score: {probability:.3f}")
