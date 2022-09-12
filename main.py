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

def graphDataPts(df, width=0.1):
    #1) Isolate and create two new subsets within each gender: those who got lung cancer and those who didn't
    #2) Make a plot for each subset showing how many in either subset had or didn't have an attribute
    
    #Current problem is that cancerTrueM is only columns, doesn't contain neccesary data in rows. Once that problem is fixed this should
    #correctly analyze... I hope. Idk what I'm really doing

    cancerTrueM = M.loc[M['LUNG_CANCER'] == "2"]
    print(cancerTrueM)
    print(cancerTrueM['AGE'])
    print(cancerTrueM['LUNG_CANCER'])

    plt.bar(cancerTrueM['AGE'], cancerTrueM['LUNG_CANCER'], color='blue')
    plt.title('Lung Cancer in Males')
    plt.xlabel('Age')
    plt.ylabel('Logged lung cancer')
    plt.figure(0)
    
    # plt.bar(F['AGE'], F['LUNG_CANCER'], color='pink')
    # plt.title('Lung Cancer in Females')
    # plt.xlabel('Age')
    # plt.ylabel('Logged lung cancer')
    # plt.figure(1)

M, F = separateGenders(df)

df['LUNG_CANCER'] = df['LUNG_CANCER'].replace({'YES': '2'})
df['LUNG_CANCER'] = df['LUNG_CANCER'].replace({'NO': '1'})

graphDataPts(df)
plt.show()
