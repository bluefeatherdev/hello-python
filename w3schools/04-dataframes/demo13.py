# W3Schools, Pandas DataFrames
import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

# refer to the named index:
print(df.loc["day2"])
