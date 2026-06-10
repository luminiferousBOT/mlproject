import os
import sys
from dataclasses import dataclass

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join(ROOT_DIR, 'artifacts', "train.csv")
    test_data_path: str=os.path.join(ROOT_DIR, 'artifacts', "test.csv")
    raw_data_path: str=os.path.join(ROOT_DIR, 'artifacts', "data.csv")
    source_data_path: str=os.path.join(ROOT_DIR, 'notebook', 'data', 'stud.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv(self.ingestion_config.source_data_path)
            logging.info('Read the dataset as a dataframe from %s', self.ingestion_config.source_data_path)

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Raw data saved at %s", self.ingestion_config.raw_data_path)

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)
