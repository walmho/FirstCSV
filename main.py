import pandas as pd
import matplotlib.pyplot as plt
import scrubFunctions as scrub
import numpy as np

# https://www.w3schools.com/python/pandas/pandas_cleaning_empty_cells.asp
# Pretty cool stuff

raw = scrub.load("survey lung cancer.csv")
df = scrub.clean(raw)

def separateGenders(df):
    dfMale = df[df['GENDER'] == "M"]
    dfFemale = df[df['GENDER'] == "F"]
    
    print(dfMale)
    print("\n")
    print(dfFemale)
    
    return dfMale, dfFemale
    
def separateSmokers(df):
    #This doesn't work for some reason so I'm ignoring it like all good coders
    dfSmoke = df[df['SMOKING'] == "2"]
    dfNo = df[df['SMOKING'] == "1"]
    
    print(dfSmoke)
    print("\n")
    print(dfNo)

def graphDataPts(df, kind, x, y, gender):
    print(df)
    
    df.plot(kind)
    plt.title(gender)

M, F = separateGenders(df)
graphDataPts(M, 'bar', 'SMOKING', list[0, 100], gender="Male")
graphDataPts(F, 'bar', 'SMOKING', list[0, 100], gender="Female")
#separateSmokers(df)