# W3Schools, Pandas Plotting, Histogram

# Three lines to make W3Schools compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df["Duration"].plot(kind = 'hist')

plt.show()

# Two lines to make W3Schools compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
