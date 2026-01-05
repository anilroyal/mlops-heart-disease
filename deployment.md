# Production Deployment

The Heart Disease Prediction API was deployed locally using Docker Desktop.

## Deployment Steps
1. Docker image was built using a Dockerfile.
2. The container was run as a background service.
3. API was exposed on port 8000.

## Commands Used
```bash
docker build -t heart-disease-api .
docker run -d -p 8000:8000 --name heart-disease-prod heart-disease-api
