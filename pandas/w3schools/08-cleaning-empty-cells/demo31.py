# W3Schools, Pandas Cleaning Empty Cells
import pandas as pd

df = pd.read_csv('data.csv')

# the value that appears most frequently:
x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = True)

print(df.to_string())
