# Heart Disease Prediction – MLOps Project

## Overview
This project demonstrates an end-to-end **MLOps pipeline** for predicting the presence of heart disease using machine learning.  
The objective is not only to build an accurate model, but also to operationalize it using **CI/CD, containerization, deployment, and monitoring** following industry best practices.

The project covers:
- Data preprocessing and exploratory data analysis (EDA)
- Model training and experiment tracking
- Automated testing and CI/CD
- Model serving via REST API
- Docker containerization
- Local Kubernetes deployment
- Monitoring and logging



## Dataset
- **Dataset Name:** UCI Heart Disease Dataset  
- **Source:** https://archive.ics.uci.edu/ml/datasets/heart+disease  

The dataset contains clinical attributes such as age, sex, cholesterol, blood pressure, ECG results, and exercise-induced angina.

### Target Variable
The original dataset contains multiple target classes.  
For this project, the target was converted into **binary classification**:
- `0` → No heart disease
- `1` → Presence of heart disease

### How to Obtain the Dataset
1. Download the dataset from the UCI repository link above.
2. Place the dataset file in the `data/` directory.
3. Use the provided notebooks/scripts for preprocessing and training.

---

## Model Training & Experiment Tracking
- Model training is performed using **Logistic Regression**.
- **MLflow** is used to track:
  - Parameters
  - Metrics (accuracy, precision, recall)
  - Trained model artifacts

This ensures reproducibility and experiment comparison.

---

## CI/CD Pipeline
A CI/CD pipeline is implemented using **GitHub Actions**.

### Pipeline Features
- Triggered on every push to the `ci-cd` branch
- Installs dependencies
- Runs unit tests using **Pytest**
- Validates code quality
- Produces logs for each workflow run

The pipeline ensures that only tested and validated code is promoted.

---

## Model Serving API
- The trained model is exposed via a **FastAPI** REST API.
- Endpoint: `/predict`
- Accepts JSON input and returns:
  - Prediction (`0` or `1`)
  - Confidence score

Swagger UI is available for interactive testing.

---

## Docker Containerization
The API is containerized using **Docker** to ensure portability and consistency.

### Build Docker Image
docker build -t heart-disease-api .

