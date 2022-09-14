import pandas as pd
# This file will probably do nothing because this dataset came from kaggle but it's good to learn how to clean them anyways

def load(file):
    dataFile = pd.read_csv(file)
    return dataFile

def clean(file):
    # Looks for bad pieces of data and removes them automagically
    noNull = file.dropna()
    # ^make inplace=True if you want to edit the original dataset. This currently creates a new var with no null values
    
    #Not dropping duplicate values as it may be messing with the age
    #cleaned = noNull.drop_duplicates()
    return noNull

# can also later make functions to replace empty values with averages rather then just delete them, detect misentered data, etc. Most of this needs
# to be practiced with a dataset that is purposefully made wrong, just to make sure that the values are being cleaned correctly
