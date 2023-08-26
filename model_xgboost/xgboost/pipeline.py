# Save trained model to pkl file
import pickle
# Import model methods
from train_model import train
from predict_model import test

data_path = "/home/leticia/GitHub/Web-Model-Prediction/model_xgboost/data/raw_data.csv"

# Train model
model = train(data_path)
# Test model
test(data_path)

# Save model to pkl file
model_pkl_file = "/home/leticia/GitHub/Web-Model-Prediction/model_xgboost/models/xgboost_model.pkl"  
with open(model_pkl_file, 'wb') as file:  
    pickle.dump(model, file)