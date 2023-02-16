import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 250, 1000)
y = np.array([10,15,50,5,10,15])

plt.subplot(2, 1, 1)
plt.pie(y)

plt.subplot(2, 1, 2)
plt.hist(x)
plt.show()

