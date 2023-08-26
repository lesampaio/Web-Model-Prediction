from pickle import load

def xgb_regressor(features) -> dict:
    """
    Runs XGBoost Regressor and returns model prediction.

    Args:
        features: User features to predict waiting time.

    Return:
        Message with waiting time prediction.
    """
    # Load model
    model = load("/home/leticia/GitHub/Web-Model-Prediction/model/xgboost_model.pkl")

    # Prediction in new features
    prediciton = model.predict(features)

    return {"message": f"The waiting time is {prediciton}"}