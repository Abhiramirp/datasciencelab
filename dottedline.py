import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([1,2,6,18])
ypoints=np.array([3,10,12,20])

plt.plot(xpoints,ypoints,'--g',marker = 'o',
         markerfacecolor = 'red')

plt.show()
