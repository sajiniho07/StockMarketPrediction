import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('res/project_data.csv')
df['<DTYYYYMMDD>'] = pd.to_datetime(df['<DTYYYYMMDD>'], format='%Y%m%d')
dayValues = np.array(df['<DTYYYYMMDD>'].tolist())
closeValues = np.array(df['<CLOSE>'].tolist())

plt.plot(dayValues, closeValues, label="f(x)")
plt.xlabel("DAYS")
plt.ylabel("CLOSE")
plt.legend()
plt.savefig('res/basic_plot.png')

dy = closeValues.copy()
dy[1:] = np.diff(closeValues)
dy[0] = dy[1]

dx = closeValues.copy()
delta_days = np.diff(dayValues)
dx[1:] = np.array([d.days for d in delta_days], dtype=int)
dx = np.abs(dx)
dx[0] = dx[1]

yprime = dy / dx

plt.plot(dayValues, yprime, label="f’(x) = dy / dx")
plt.xlabel("DAYS")
plt.ylabel("DERIVATIVE")
plt.title("Derivative of close on day values")
plt.legend()
plt.savefig('res/derivative_plot.png')
plt.show()

tenSets = np.array([closeValues[i : i+10] for i in range(len(closeValues) - 9)])

predictSet = tenSets[:-1, 9] < tenSets[1:, 0]

#print(tenSets, tenSets.shape)
#print(predictSet, predictSet.shape)
