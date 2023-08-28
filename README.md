# Web Application - Model Prediction
Web application that receives user data and predicts their waiting time in the bank queue. MLOps tools and services are being used: *FastAPI, Docker, Python, AWS, Streamlit.*

- app: FastAPI Web app that receives user data and predicts their waiting time in the bank queue.
- dockerfile: Dockerfile to run FastAPI app.
- machine learning model: XGBoost Regressor model that predicts user queue waiting time in the bank queue. The machine learning model code can be found in the [Data Science Projects](https://github.com/lesampaio/Data-Science-Projects) repository.

## FastAPI

**How to Run API:**

`uvicorn main:app --reload`

### API Directory Structure

        ├── app                         
        │   ├── __init__.py             <- This file makes "app" a "Python package"
        │   ├── main.py                 <- "main" module, e.g. import app.main
        │   └── routers                 <- "routers" is a "Python subpackage"
        │   │   ├── __init__.py        
        │   │   └── ml_model.py         <- Machine learning route
        │   │   
        │   └── config                  <- Database sessions
        │   │           
        │   └── xgboost_model           <- ML model packages
        │   │   ├── __init__.py    
        │   │   ├── xgboost.py          <- Implemented trained model
        │   │   └── xgboost_model.pkl   <- Trained and serialized model
        │   │
        │   └── models                  <- SQLAlchemy (Database) models
        │   │   └── __init__.py         
        │   │
        │   └── schemas                 <- Schemas for data validation
        │   │   └──__init__.py  
        │   │   
        │   └── tests                   <- Tests folder
        │       └── __init__.py  