import pandas as pd

# Preprocessing - Split train and test data
from sklearn.model_selection import train_test_split

def preprocess(data_path) -> tuple:
    """
    
    Args:
        data_path: Raw data path.
    
    Return:
        X_train, X_test: Train and test features. 
        y_train, y_test: Train and test labels.

        Tuple: X_train, X_test, y_train, y_test
    """
    # Load data
    data = pd.read_csv(data_path)

    # Drop 'num' column, it's not needed
    data.drop(columns=["num"], inplace=True)
    # Categorical to binary
    data = pd.get_dummies(data=data, dtype=int)
    
    # Define feature columns
    X = data.loc[:, data.columns != "waiting_time"]
    # Define label column
    y = data["waiting_time"]

    # Split train and test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    return X_train, X_test, y_train, y_test