# Routers dedicated to model operations
from fastapi import APIRouter
# Xgboost model
from xgboost_model.xgboost import xgb_regressor
# Schemas
from schemas.model import ModelInputFeatures

router = APIRouter(
    prefix="/model",
    tags=["model"],
    responses={404: {"description": "Endpoint not found."}}
)

@router.post("/send_features")
async def send_features(features: ModelInputFeatures):
    """
    Send feature data to be model input. Validate data with Data Model pydantic.

    Args:
        features: Dict with model input features.
        [bank, week, day, arrival_time, time_spent, exit_time, people_in_queue]
    """

    return features

@router.get("/output")
async def return_output(features):
    """
    Returns model prediction output.

    Args:
        features: List with model input features.
        [bank, week, day, arrival_time, time_spent, exit_time, people_in_queue]

    Return:
        Model prediction output.
    """
    # Make model prediction and return message
    output_message = xgb_regressor(features)

    return output_message