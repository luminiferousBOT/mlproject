import os
import sys
import pickle

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from src.exception import CustomException
from src.logger import logging
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score


class ModelTrainer:
    def __init__(self):
        self.model_path = os.path.join(ROOT_DIR, "artifacts", "model.pkl")
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)

    def initiate_model_trainer(self, X_train, X_test, y_train, y_test):
        try:
            model = RandomForestRegressor(n_estimators=50, random_state=42)
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            score = r2_score(y_test, y_pred)

            with open(self.model_path, "wb") as f:
                pickle.dump(model, f)

            logging.info("Model training completed with R2 score: %.4f", score)
            return self.model_path, score
        except Exception as e:
            raise CustomException(e, sys)
