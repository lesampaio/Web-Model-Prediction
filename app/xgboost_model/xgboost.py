from pickle import load

def xgb_regressor(features) -> dict:
    """
    Runs XGBoost Regressor and returns model prediction.

    Args:
        features: User features to predict waiting time.

    Return:
        Waiting time prediction.
    """
    # Load model
    model = load("app/xgboost_model/xgboost_model.pkl")

    # Prediction in new features
    prediciton = model.predict(features)

    return prediciton