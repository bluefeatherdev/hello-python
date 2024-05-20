# W3Schools, Pandas Plotting, Scatter Plot

"""
Do not use if you are working on your personal computer:
import sys
import matplotlib
matplotlib.use('Agg')
...
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

Use instead:
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')

plt.show()
