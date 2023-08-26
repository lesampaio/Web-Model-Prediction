# Routers dedicated to model operations
from fastapi import APIRouter

router = APIRouter(
    prefix="/model",
    tags=["model"],
    responses={404: {"description": "Endpoint not found."}}
)

@router.post("/read_features")
async def read_features(features):
    """
    Receives dictionary containing features that will serve as model input.

    Args:
        features: Dictionary with input features.
    """
    return {"status": "ok", "message": "Features received successfully!"}

@router.get("/output")
async def return_output(model_output):
    """
    Returns model output.

    Args:
        features: Dictionary with input features.
    """
    return {"status": "ok", "message": "Model output."}

@router.get("/metric_result")
async def return_output(metric):
    """
    Returns model metric result.
    """
    return {"status": "ok","message": "Model metric result."}