import logging
# Routers dedicated to model operations
from fastapi import APIRouter, HTTPException
# Xgboost model
from xgboost_model.xgboost import xgb_regressor
# Schemas
from schemas.model import ModelInputFeatures
from pydantic import ValidationError

router = APIRouter(
    prefix="/model",
    tags=["model"],
    responses={404: {"description": "Endpoint not found."}}
)

@router.post("/send-features")
def send_features(features: ModelInputFeatures):
    """
    Send feature data to be model input. Validate data with Data Model pydantic.

    Args:
        features: ModelInputFeatures instance.
    """

    try:
        logging.debug("Initializing features validation.")
        # "features" is already a validated instance of ModelInputFeatures
        features

        # TODO: Connect to database
        # TODO: Insert data into database

        return {"message": "Features validated."}
    
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/output")
def return_output(features):
    """
    Returns model prediction output.

    Args:
        features: List with model input features.
        [bank, week, day, arrival_time, time_spent, exit_time, people_in_queue]

    Return:
        Model prediction output.
    """
    # TODO: Get features from Database

    # Make model prediction and return message
    output = xgb_regressor(features)

    return {"message": output}