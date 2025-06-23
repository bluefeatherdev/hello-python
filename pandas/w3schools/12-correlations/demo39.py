# W3Schools, Pandas Correlations
import pandas as pd

df = pd.read_csv('data.csv')

print(df.corr())
