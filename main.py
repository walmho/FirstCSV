import pandas as pd
import matplotlib as plt
import scrubFunctions as scrub

#https://www.w3schools.com/python/pandas/pandas_cleaning_empty_cells.asp
#Pretty cool stuff

raw = scrub.load("survey lung cancer.csv")
df = scrub.clean(raw)


