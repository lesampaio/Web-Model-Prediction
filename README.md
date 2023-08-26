# Web Application - Model Prediction
Web application that receives patient's data and predicts his queue waiting time. MLOps tools and services are being used: *FastAPI, Docker, Python, AWS, Streamlit.*

- app: FastAPI Web app that receives patient's data and predicts his queue waiting time.
- model_xgboost: XGBoost Regressor model that predicts patient queue waiting time.
- dockerfile: Dockerfile to run FastAPI app.

## FastAPI

**Run API**

`uvicorn main:app --reload`

### API Directory Structure

        ├── app                  <- "app" is a Python package
        │   ├── __init__.py      <- this file makes "app" a "Python package"
        │   ├── main.py          <- "main" module, e.g. import app.main
        │   ├── dependencies.py  <- "dependencies" module, e.g. import app.dependencies
        │   └── routers          <- "routers" is a "Python subpackage"
        │   │   ├── __init__.py  <- makes "routers" a "Python subpackage"
        │   │   ├── items.py     <- "items" submodule, e.g. import app.routers.items
        │   │   └── users.py     <- "users" submodule, e.g. import app.routers.users
        │   └── internal         <- "internal" is a "Python subpackage"
        │   │   ├── __init__.py  <- makes "internal" a "Python subpackage"
        │   │   └── admin.py     <- "admin" submodule, e.g. import app.internal.admin
        │   │
        │   └── schemas          <- Schemas for data validation
        │   │   └──__init__.py  
        │   └── tests            <- Tests folder
        │       └── __init__.py  

## Machine Learning Model - XGBoost

### ML XGBoost Regressor Directory Structure

        ├── model_xgboost               <- "model_xgboost" XGBoost model package
        │   ├── __init__.py             <- This file makes "model_xgboost" a "Python package"
        │   └── data                    <- Data from third party sources
        │   │   └── raw_data.csv
        │   │
        │   ├── models                  <- Trained and serialized models, model predictions, or model summaries
        │   │
        │   └── requirements.txt        <- The requirements file for reproducing the analysis environment, e.g.
        │   │                     generated with `pip freeze > requirements.txt`
        │   │
        │   └── xgboost                 <- Scripts to train models and then use trained models to make predictions
        │   │   │   __init__.py         <- Makes "xgboost" a "Python subpackage"      
        │   │   ├── pipeline.py         <- Run model pipeline          
        │   │   ├── preprocess_data.py        
        │   │   ├── predict_model.py
        │   │   └── train_model.py
        │   │
        │   └── tests                   <- Tests folder