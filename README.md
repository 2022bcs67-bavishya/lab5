# Lab 2 - MLOps Pipeline

**Name:** Bavishya  
**Roll No:** 2022BCS0067

## Project Overview

This repository contains a complete MLOps pipeline for wine quality prediction using machine learning models. The project includes:

- Model training with multiple experiments
- FastAPI-based prediction API
- Docker containerization
- CI/CD pipeline with GitHub Actions
- Automated model evaluation and tracking

## Repository Structure

```
lab2/
├── .github/
│   └── workflows/
│       └── train.yml          # GitHub Actions workflow
├── data/
│   └── winequality-red.csv    # Wine quality dataset
├── outputs/                    # Model outputs and results
├── train.py                    # Training script
├── requirements.txt            # Python dependencies
├── app.py                      # FastAPI application
├── Dockerfile                  # Docker configuration
└── README.md                   # This file
```

## Features

- **Multiple Model Types:** Random Forest and Ridge Regression
- **Experiment Tracking:** Multiple experiments with different hyperparameters
- **REST API:** FastAPI-based prediction endpoint
- **Containerization:** Docker image for easy deployment
- **CI/CD:** Automated training pipeline with GitHub Actions

## Docker Hub

Docker image available at: https://hub.docker.com/r/2022bcs0067/wine-quality-api

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run training: `python lab2/train.py`
4. Start API: `uvicorn app:app --reload`

## Usage

### Training Models

```bash
cd lab2
python train.py
```

### Running API

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

### Docker

```bash
docker pull 2022bcs0067/wine-quality-api:v1
docker run -p 8000:8000 2022bcs0067/wine-quality-api:v1
```

## API Documentation

Once the API is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## License

This project is for educational purposes.
