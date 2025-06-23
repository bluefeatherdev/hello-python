# W3Schools, Pandas Cleaning Wrong Data
import pandas as pd

df = pd.read_csv('data.csv')

df.loc[7, 'Duration'] = 45

print(df.to_string())
