import sys
import matplotlib
matplotlib.use('QtAgg')

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 150])

plt.plot(xpoints, ypoints)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()