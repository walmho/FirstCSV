import pandas as pd
import matplotlib.pyplot as plt
import scrubFunctions as scrub
import numpy as np

pd.options.mode.chained_assignment = None  # default='warn'

# https://www.w3schools.com/python/pandas/pandas_cleaning_empty_cells.asp
# Pretty cool stuff

raw = scrub.load("survey lung cancer.csv")
df = scrub.clean(raw)

def separateGenders(df):
    dfMale = df[df['GENDER'] == "M"]
    dfFemale = df[df['GENDER'] == "F"]
    
    # print(dfMale)
    # print("\n")
    # print(dfFemale)
    
    return dfMale, dfFemale
    
def separateSmokers(df):
    #This doesn't work for some reason so I'm ignoring it like all good coders
    dfSmoke = df[df['SMOKING'] == "2"]
    dfNo = df[df['SMOKING'] == "1"]
    
    print(dfSmoke)
    print("\n")
    print(dfNo)

def graphDataPts(df, x, y, gender, width=0.1):
    print(x)
    print("\n\n")
    print(y)

    plt.bar(x, y)
    plt.title("Data for {}".format(gender))

M, F = separateGenders(df)

df['LUNG_CANCER'] = df['LUNG_CANCER'].replace({'YES': '2'})
df['LUNG_CANCER'] = df['LUNG_CANCER'].replace({'NO': '1'})
y = df['LUNG_CANCER']

graphDataPts(df, df['SMOKING'], y, M)
plt.show()
