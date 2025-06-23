# W3Schools, Pandas Cleaning Empty Cells
import pandas as pd

df = pd.read_csv('data.csv')

df.dropna(inplace = True) # change the original DataFrame

print(df.to_string())
