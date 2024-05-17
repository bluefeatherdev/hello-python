# W3Schools, Pandas Cleaning Empty Cells
import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())
