"""
Model-serving API for Heart Disease Classification
"""

import logging
import time
import joblib
import pandas as pd

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from prometheus_client import Counter, Histogram, generate_latest
from starlette.responses import Response

# ------------------------------------------------------------------
# Logging Configuration
# ------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# ------------------------------------------------------------------
# FastAPI App Initialization
# ------------------------------------------------------------------
app = FastAPI(
    title="Heart Disease Prediction API",
    description="API for predicting presence of heart disease",
    version="1.0.0"
)

# ------------------------------------------------------------------
# Prometheus Metrics
# ------------------------------------------------------------------
REQUEST_COUNT = Counter(
    "api_requests_total",
    "Total number of API requests",
    ["method", "endpoint"]
)

REQUEST_LATENCY = Histogram(
    "api_request_latency_seconds",
    "API request latency in seconds"
)

# ------------------------------------------------------------------
# Load Trained Model
# ------------------------------------------------------------------
MODEL_PATH = "src/heart_disease_model.pkl"
model = joblib.load(MODEL_PATH)

FEATURE_COLUMNS = [
    "age", "sex", "cp", "trestbps", "chol",
    "fbs", "restecg", "thalach", "exang",
    "oldpeak", "slope", "ca", "thal"
]

# ------------------------------------------------------------------
# Request Schema
# ------------------------------------------------------------------
class PatientInput(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

# ------------------------------------------------------------------
# Middleware for Logging & Metrics
# ------------------------------------------------------------------
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time

    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.url.path
    ).inc()

    REQUEST_LATENCY.observe(duration)

    logging.info(
        f"{request.method} {request.url.path} "
        f"Status={response.status_code} "
        f"Latency={duration:.4f}s"
    )

    return response

# ------------------------------------------------------------------
# Root Endpoint → Redirect to Swagger UI
# ------------------------------------------------------------------
@app.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url="/docs")

# ------------------------------------------------------------------
# Prediction Endpoint
# ------------------------------------------------------------------
@app.post("/predict")
def predict(input_data: PatientInput):
    """
    Accepts patient clinical data and returns:
    - prediction (0 = No disease, 1 = Disease)
    - confidence score
    """
    df = pd.DataFrame([input_data.dict()], columns=FEATURE_COLUMNS)

    prediction = int(model.predict(df)[0])
    confidence = float(model.predict_proba(df)[0][1])

    return {
        "prediction": prediction,
        "confidence": round(confidence, 4)
    }

# ------------------------------------------------------------------
# Metrics Endpoint
# ------------------------------------------------------------------
@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type="text/plain"
    )
