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

def plotOccurences():
    #Graphs # of times patients of age X had lung cancer for both males and females
    occurenceCtM = (M["AGE"].value_counts()).sort_index(axis=0, ascending=True, inplace=False)
    plt.figure(0)
    occurenceCtM.plot(kind="bar", color="blue")
    plt.title("Lung Cancer in Males")
    plt.xlabel("Age")
    plt.ylabel("# of Cases")
    
    occurenceCtF = (F["AGE"].value_counts()).sort_index(axis=0, ascending=True, inplace=False)
    plt.figure(1)
    occurenceCtF.plot(kind="bar", color="pink")
    plt.title("Lung Cancer in Females")
    plt.xlabel("Age")
    plt.ylabel("# of Cases")

#converts yes/no values to 1 or 2 for graphability
df["LUNG_CANCER"] = df["LUNG_CANCER"].replace({"YES": "2"})
df["LUNG_CANCER"] = df["LUNG_CANCER"].replace({"NO": "1"})

M, F = separateGenders(df)

plotOccurences()
plt.show()
