# W3Schools, Pandas DataFrames
import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# load data into a DataFrame object:
df = pd.DataFrame(data)

# refer to the row index:
print(df.loc[0])
