# Preprocess data
from preprocess_data import preprocess
# Import trained model
from train_model import train
# Model metric
from sklearn.metrics import mean_squared_error

def test(raw_data_file_path):
    """
    Run this method to test model.
    
    Args:
        raw_data_file_path: Raw data path file.

    Return:
        model: The XGBRegressor model class.
    """
    # Preprocess raw data and get X_test and y_test
    X_train, X_test, y_train, y_test = preprocess(raw_data_file_path)

    # Instantiate trained model
    model = train(raw_data_file_path)

    # Predict values with new data
    y_pred = model.predict(X_test)

    # Print model test score MSE
    print("Evaluate model on test data.")
    print(f"Model score MSE in test data: {round( mean_squared_error(y_test, y_pred), 2 )} minutes")