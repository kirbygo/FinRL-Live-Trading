import pathlib

#import finrl

import pandas as pd
import datetime
import os
pd.options.display.max_rows = 10
pd.options.display.max_columns = 10

#PACKAGE_ROOT = pathlib.Path(finrl.__file__).resolve().parent
PACKAGE_ROOT = pathlib.Path().resolve().parent

TRAINED_MODEL_DIR = PACKAGE_ROOT / r"trained_models"
#DATASET_DIR = PACKAGE_ROOT / "data"

# data
#TRAINING_DATA_FILE = "data/ETF_SPY_2009_2020.csv"
TRAINING_DATA_FILE = r"data/dow_30_2009_2020.csv"

now = datetime.datetime.now().strftime("%d-%m-%y-%H-%M-%S")
TRAINED_MODEL_DIR = rf"trained_models/{now}"
os.makedirs(TRAINED_MODEL_DIR)
TURBULENCE_DATA = r"data/dow30_turbulence_index.csv"

TESTING_DATA_FILE = r"test.csv"


