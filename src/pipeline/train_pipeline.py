import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.logger import logging


def run_training_pipeline():
    logging.info("Starting training pipeline")
    ingestion = DataIngestion()
    train_path, test_path = ingestion.initiate_data_ingestion()

    transformation = DataTransformation()
    X_train, X_test, y_train, y_test = transformation.initiate_data_transformation(train_path, test_path)

    trainer = ModelTrainer()
    model_path, score = trainer.initiate_model_trainer(X_train, X_test, y_train, y_test)

    logging.info("Training pipeline completed. Model saved to %s", model_path)
    print(f"Training completed. Model saved to: {model_path}")
    print(f"R2 score: {score:.4f}")


if __name__ == "__main__":
    run_training_pipeline()
