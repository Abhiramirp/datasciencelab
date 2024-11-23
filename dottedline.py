import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,6,18])
y=np.array([3,10,12,20])

plt.plot(x,y,'--g',marker = 'o',
         markerfacecolor = 'red')

plt.show()
