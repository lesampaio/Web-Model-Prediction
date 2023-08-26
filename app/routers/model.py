# Routers dedicated to model operations
from fastapi import APIRouter
# Xgboost model
from ml_model.xgboost import xgb_regressor
# Schemas
from schemas.model import ModelInputFeatures

router = APIRouter(
    prefix="/model",
    tags=["model"],
    responses={404: {"description": "Endpoint not found."}}
)

@router.get("/output")
async def return_output(features):
    """
    Loads model and returns model prediction output.

    Args:
        features: List with model input features.
        [bank, week, day, arrival_time, time_spent, exit_time, people_in_queue]
    """
    # Validate features
    ModelInputFeatures(features)

    # Make model prediction and return message
    output_message = xgb_regressor(features)

    return output_message