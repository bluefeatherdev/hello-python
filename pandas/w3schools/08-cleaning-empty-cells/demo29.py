# W3Schools, Pandas Cleaning Empty Cells
import pandas as pd

df = pd.read_csv('data.csv')

# the average value (the sum of all values divided by number of values):
x = df["Calories"].mean() 

df["Calories"].fillna(x, inplace = True)

print(df.to_string())
