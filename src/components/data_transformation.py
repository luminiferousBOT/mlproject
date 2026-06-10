import os
import sys
import pandas as pd

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from src.exception import CustomException
from src.logger import logging


class DataTransformation:
    def __init__(self):
        self.root_dir = ROOT_DIR

    def initiate_data_transformation(self, train_path: str, test_path: str):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Loaded train and test data for transformation")

            target_column = "math_score"
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            train_df = pd.get_dummies(train_df, columns=categorical_columns, drop_first=True)
            test_df = pd.get_dummies(test_df, columns=categorical_columns, drop_first=True)

            test_df = test_df.reindex(columns=train_df.columns, fill_value=0)

            X_train = train_df.drop(columns=[target_column])
            y_train = train_df[target_column]
            X_test = test_df.drop(columns=[target_column])
            y_test = test_df[target_column]

            logging.info("Data transformation completed")
            return X_train, X_test, y_train, y_test
        except Exception as e:
            raise CustomException(e, sys)
