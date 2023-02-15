import sys
import matplotlib
matplotlib.use('QtAgg')

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6, 80, 10])
ypoints = np.array([20, 50, 10, 40])

plt.plot (xpoints)  
plt.plot(ypoints)   
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()