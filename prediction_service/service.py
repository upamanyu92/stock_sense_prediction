import pandas as pd
from prediction_service.model import PredictionModel

class PredictionService:
    def __init__(self):
        self.model = PredictionModel()

    def preprocess(self, data):
        # Implement any preprocessing you need here
        df = pd.DataFrame(data)
        # Example: Convert date to timestamp, fill missing values, etc.
        return df

    def make_prediction(self, data):
        preprocessed_data = self.preprocess(data)
        predictions = self.model.predict(preprocessed_data)
        return predictions.tolist()
