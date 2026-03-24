# Hotel Reservation Prediction

A machine learning project that predicts hotel booking cancellations using a complete MLOps pipeline with data ingestion, preprocessing, model training, and a web interface for predictions.

## Overview

This project implements an end-to-end machine learning solution for predicting whether a hotel reservation will be cancelled. It demonstrates best practices in MLOps, including data engineering, feature engineering, model training with hyperparameter tuning, experiment tracking, and containerized deployment.

## Problem Statement

Hotel cancellations are a significant challenge in the hospitality industry, affecting revenue planning and resource allocation. This project builds a predictive model to identify likely cancellations based on reservation characteristics, enabling proactive business decisions.

## Key Features

- **Complete ML Pipeline**: Automated data ingestion, preprocessing, feature engineering, and model training
- **Data Processing**: 
  - Label encoding for categorical features
  - Skewness handling for numerical features
  - SMOTE-based class balancing to handle imbalanced data
  - Automated feature selection using Random Forest importance
- **Model Training**: LightGBM classifier with hyperparameter tuning via RandomizedSearchCV
- **Experiment Tracking**: MLflow integration for logging parameters, metrics, and artifacts
- **Web Interface**: Flask-based application for real-time predictions
- **Containerization**: Docker support with automated model training
- **CI/CD Pipeline**: Jenkins integration for automated build, test, and deployment to Google Cloud Run

## Project Structure

Hotel_Reservation_Prediction/ ├── src/ # Core ML pipeline modules │ ├── data_ingestion.py # Download and split data from GCP Storage │ ├── data_preprocessing.py # Feature engineering and data preparation │ ├── model_training.py # Model training with hyperparameter tuning │ ├── custom_exception.py # Custom exception handling │ └── logger.py # Logging configuration ├── pipeline/ │ └── training_pipeline.py # Orchestrates the complete ML pipeline ├── config/ │ ├── config.yaml # Data and feature configuration │ ├── model_params.py # LightGBM hyperparameter distributions │ └── path_config.py # Artifact and data paths ├── utils/ │ └── common_fuctions.py # Utility functions (YAML reading, data loading) ├── templates/ │ └── index.html # Web interface for predictions ├── application.py # Flask web application ├── Dockerfile # Container configuration ├── Jenkinsfile # CI/CD pipeline configuration ├── requirements.txt # Python dependencies ├── setup.py # Package setup configuration └── notebook/ # Jupyter notebook and training data

