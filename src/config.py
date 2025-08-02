import os

# Set a fixed seed for reproducibility
SEED = 42

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATA_DIR = os.path.join(BASE_DIR, 'data')
RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')
INTERIM_DATA_DIR = os.path.join(DATA_DIR, 'interim')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')

OUTPUTS_DIR = os.path.join(BASE_DIR, 'outputs')
MODELS_DIR = os.path.join(OUTPUTS_DIR, 'models')
SUBMISSIONS_DIR = os.path.join(OUTPUTS_DIR, 'submissions')

EXPERIMENTS_DIR = os.path.join(BASE_DIR, 'experiments')

# File names
TRAIN_FILE = os.path.join(RAW_DATA_DIR, 'train.csv')
TEST_FILE = os.path.join(RAW_DATA_DIR, 'test.csv')

# Target column
TARGET_COL = 'y'
ID_COL = 'id'

# Cross-validation
N_SPLITS = 5
