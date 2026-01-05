"""
Unit tests for inference pipeline.
Ensures model loads correctly and produces valid outputs.
"""

import pandas as pd
from pathlib import Path
import joblib


def test_model_inference():
    """
    Test that the trained model:
    - Loads successfully
    - Produces a binary prediction
    - Produces a valid probability score
    """

    model_path = Path(__file__).resolve().parent.parent / "src" / "heart_disease_model.pkl"
    model = joblib.load(model_path)

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

    prediction = model.predict(sample_input)[0]
    probability = model.predict_proba(sample_input)[0][1]

    assert prediction in [0, 1]
    assert 0.0 <= probability <= 1.0
