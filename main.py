import pandas as pd
import matplotlib.pyplot as plt
import scrubFunctions as scrub
import numpy as np

pd.options.mode.chained_assignment = None  # default="warn"

# https://www.w3schools.com/python/pandas/pandas_cleaning_empty_cells.asp
# Pretty cool stuff

raw = scrub.load("survey lung cancer.csv")
df = scrub.clean(raw)

def separateGenders(df):
    dfMale = df[df["GENDER"] == "M"]
    dfFemale = df[df["GENDER"] == "F"]

    return dfMale, dfFemale
    
def separateSmokers(df):
    #This doesn"t work for some reason so I"m ignoring it like all good coders
    dfSmoke = df[df["SMOKING"] == "2"]
    dfNo = df[df["SMOKING"] == "1"]
    
    print(dfSmoke)
    print("\n")
    print(dfNo)

def graphDataPts(w):
    #1) Isolate and create two new subsets within each gender: those who got lung cancer and those who didn"t
    #2) Make a plot for each subset showing how many inLUNG_CANCER either subset had or didn"t have an attribute

    occurenceCtM = (M["AGE"].value_counts()).sort_index(axis=0, ascending=True, inplace=False)
    plt.figure(0)
    occurenceCtM.plot(kind="bar", color="blue")
    plt.title("Lung Cancer in Males")
    plt.xlabel("Age")
    plt.ylabel("Logged lung cancer")
    
    occurenceCtF = (F["AGE"].value_counts()).sort_index(axis=0, ascending=True, inplace=False)
    plt.figure(1)
    occurenceCtF.plot(kind="bar", color="pink")
    plt.title("Lung Cancer in Females")
    plt.xlabel("Age")
    plt.ylabel("Logged lung cancer")

df["LUNG_CANCER"] = df["LUNG_CANCER"].replace({"YES": "2"})
df["LUNG_CANCER"] = df["LUNG_CANCER"].replace({"NO": "1"})

M, F = separateGenders(df)

graphDataPts(0.3)
plt.show()
