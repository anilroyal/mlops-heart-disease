## Group 119
Contribution in Assignment  
### G.Anil Kumar - 2023aa05757 - 100%
### Abhishek Lalwani 2024AA05248 - 100%
### Manaswee Adwant - 2024aa05859 - 100%
### Gaurav Pathak - 2024aa05031 - 100%
### Jagadish Bala - 2024aa05452 - 100%

# Heart Disease Prediction – MLOps Assignment

## Overview
This project demonstrates an end-to-end MLOps workflow for heart disease prediction using machine learning.

## Components
- Model training and evaluation
- CI/CD pipeline using GitHub Actions
- FastAPI-based model-serving API
- Docker containerization
- Local production deployment using Docker Desktop
- Monitoring with Prometheus-compatible metrics

## Running the Application

docker build -t heart-disease-api .
docker run -p 8000:8000 heart-disease-api
