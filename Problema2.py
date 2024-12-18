#Scris pe w3schools
#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()
plt.show()

df[:5].plot()
plt.show()

df[-10:].plot()
plt.plot(df[-10:].iloc[0, 1])
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

