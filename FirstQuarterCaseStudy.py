import pandas as pd
import numpy as npy
import matplotlib.pyplot as plt
from scipy import stats

# reading all data
data = pd.read_csv("AP Statistics Day 1 Survey 2023 - 2024.csv")

# choosing data sets
print(data.columns[22])  # parent political affiliation
print(data.columns[32])  # us states been in

parentPolitics = data[
    "How would you describe the political affiliation of your parents?"
]
usStates = data["Approximately how many of the 50 United States have you been in?"]

# sorting into groups
print(usStates.plot(kind="hist"))
