import pandas as pd
from src.config import TRAIN_FILE, TEST_FILE

def load_train_data():
    return pd.read_csv(TRAIN_FILE)

def load_test_data():
    return pd.read_csv(TEST_FILE)
