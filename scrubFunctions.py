import pandas as pd
# This file will probably do nothing because this dataset came from kaggle but it's good to learn how to clean them anyways

def load(file):
    dataFile = pd.read_csv(file)
    return dataFile

def clean(file):
    # Looks for bad pieces of data and removes them automagically
    noNull = file.dropna()
    # ^make inplace=True if you want to edit the original dataset. This currently creates a new var with no null values
    cleaned = noNull.drop_duplicates()
    return cleaned

# can also later make functions to replace empty values with averages rather then just delete them, detect misentered data, etc.
