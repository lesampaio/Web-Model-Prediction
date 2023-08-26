# Preprocess data
from preprocess_data import preprocess

# Boosting algorithm
import xgboost
# Cross-validation
from sklearn.model_selection import RepeatedKFold
# Evaluate a score by cross-validation
from sklearn.model_selection import cross_val_score
# Model metric
from sklearn.metrics import mean_squared_error
from numpy import absolute

def train(raw_data_file_path):
    """
    Run this method to train model.
    
    Args:
        raw_data_file_path: Raw data path file.

    Return:
        model: The XGBRegressor model class.
    """
    # Preprocess raw data and get X_train and y_train
    X_train, X_test, y_train, y_test = preprocess(raw_data_file_path)

    # Create regression model
    model = xgboost.XGBRegressor()

    # Cross-validation
    cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)

    # Evaluate model score
    scores = cross_val_score(model, X_train, y_train, scoring="neg_mean_squared_error", cv=cv, n_jobs=-1)

    # Force scores to be positive
    scores = absolute(scores)
    # Print model evaluation in Train-Validation datasets
    print(f"Train-Validation dataset -> Mean MSE: {round( scores.mean(), 2 )} minutes --- Standard Deviation: {round( scores.std(), 2 )}")
    print("From this we can estimate the test error as the training and validation data are not overlapping.")

    model.fit(X_train, y_train)

    return model