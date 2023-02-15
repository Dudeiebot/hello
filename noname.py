import sys
import matplotlib
matplotlib.use('QtAgg')

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6, 80, 10])
ypoints = np.array([20, 50, 10, 40])

plt.subplot(1, 2, 1)
plt.plot(xpoints)  
plt.plot(ypoints) 

x = np.array([3, 9, 6, 12])
y = np.array([20, 60, 40, 100])

plt.subplot(1, 2, 2)  #talking about rows and columns that means these have 1 row and 2 columns
plt.plot(x)
plt.plot(y)

plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()