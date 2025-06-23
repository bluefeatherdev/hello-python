# W3Schools, Pandas Cleaning Empty Cells
import pandas as pd

df = pd.read_csv('data.csv')

# Replace NULL values in the "Calories" columns with the number 130:
df["Calories"].fillna(130, inplace = True)

print(df.to_string())
