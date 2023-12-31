# FastAPI is a Python class that provides all the functionality for your API
from fastapi import FastAPI
# Import model router
from routers import ml_model

# Instantiate FastAPI class
app = FastAPI()

# Include router
app.include_router(ml_model.router)

# Define HTTP operation to apply into endpoint
@app.get("/")
# Create endpoint or router
async def root():
    return {"message": "Home page!"}