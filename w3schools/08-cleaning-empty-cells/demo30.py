# W3Schools, Pandas Cleaning Empty Cells
import pandas as pd

df = pd.read_csv('data.csv')

# the value in the middle, after you have sorted all values ascending:
x = df["Calories"].median()

df["Calories"].fillna(x, inplace = True)

print(df.to_string())
