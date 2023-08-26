# Web Application - Model Prediction
Web application that receives user data and predicts their waiting time in the bank queue. MLOps tools and services are being used: *FastAPI, Docker, Python, AWS, Streamlit.*

- app: FastAPI Web app that receives user data and predicts their waiting time in the bank queue.
- dockerfile: Dockerfile to run FastAPI app.
- model: XGBoost Regressor model that predicts user queue waiting time in the bank queue. The machine learning model code can be found in the [Data Science Projects](https://github.com/lesampaio/Data-Science-Projects) repository.

## FastAPI

**How to Run API:**

`uvicorn main:app --reload`

### API Directory Structure

        ├── app                         <- "app" is a Python package
        │   ├── __init__.py             <- this file makes "app" a "Python package"
        │   ├── main.py                 <- "main" module, e.g. import app.main
        │   ├── dependencies.py         <- "dependencies" module, e.g. import app.dependencies
        │   └── routers                 <- "routers" is a "Python subpackage"
        │   │   ├── __init__.py         <- makes "routers" a "Python subpackage"
        │   │   └── users.py            <- "users" submodule, e.g. import app.routers.users
        │   │   
        │   └── ml_model                <- "routers" is a "Python subpackage"
        │   │   ├── __init__.py         <- makes "ml_model" a "Python subpackage"
        │   │   ├── xgboost.py          <- Runs the model
        │   │   └── xgboost_model.pkl   <- Trained and serialized model
        │   │   
        │   └── internal                <- "internal" is a "Python subpackage"
        │   │   ├── __init__.py         <- makes "internal" a "Python subpackage"
        │   │   └── admin.py            <- "admin" submodule, e.g. import app.internal.admin
        │   │
        │   └── schemas                 <- Schemas for data validation
        │   │   └──__init__.py  
        │   │   
        │   └── tests                   <- Tests folder
        │       └── __init__.py  