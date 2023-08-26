from pydantic import BaseModel

# TODO: Implement pydantic model class.
class ModelInputFeatures(BaseModel):
    """
    Validate model input features.
    """
    var1: str
    var2: int