# W3Schools, Pandas Removing Duplicates
import pandas as pd

df = pd.read_csv('data.csv')

print(df.duplicated())
