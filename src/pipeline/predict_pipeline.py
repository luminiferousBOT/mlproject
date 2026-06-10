import os
import sys
import pickle

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from src.logger import logging


class PredictPipeline:
    def __init__(self):
        self.model_path = os.path.join(ROOT_DIR, "artifacts", "model.pkl")

    def load_model(self):
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Model file not found at {self.model_path}")
        with open(self.model_path, "rb") as f:
            model = pickle.load(f)
        logging.info("Loaded model from %s", self.model_path)
        return model

    def predict(self, X):
        model = self.load_model()
        predictions = model.predict(X)
        logging.info("Generated predictions for input data")
        return predictions


if __name__ == "__main__":
    print("Predict pipeline is available after training a model.")
