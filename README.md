# Web Application - Model Prediction
Web application that predicts a customer's time in line. MLOps tools and services are being used: FastAPI, AWS, Docker, Python, Streamlit.

## FastAPI

Run API:

`uvicorn main:app --reload`

API Project Organization
----

        ├── app                  # "app" is a Python package
        │   ├── __init__.py      # this file makes "app" a "Python package"
        │   ├── main.py          # "main" module, e.g. import app.main
        │   ├── dependencies.py  # "dependencies" module, e.g. import app.dependencies
        │   └── routers          # "routers" is a "Python subpackage"
        │   │   ├── __init__.py  # makes "routers" a "Python subpackage"
        │   │   ├── items.py     # "items" submodule, e.g. import app.routers.items
        │   │   └── users.py     # "users" submodule, e.g. import app.routers.users
        │   └── internal         # "internal" is a "Python subpackage"
        │   │   ├── __init__.py  # makes "internal" a "Python subpackage"
        │   │   └── admin.py     # "admin" submodule, e.g. import app.internal.admin
        │   └── schemas          # Schemas for data validation
        │   │   ├── __init__.py  
        │   └── tests            # Tests folder
        │   │   ├── __init__.py  

----