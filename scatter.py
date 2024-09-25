import matplotlib.pyplot as plt
import numpy as np
maths=np.array([88, 92, 80, 89, 100, 80, 60, 100, 80, 34])
science=np.array([35, 79, 79, 48, 100, 88, 32, 45, 20, 30])
colors=np.array (['red','green','blue','pink','black','grey','violet','beige','yellow','orange'])
plt.scatter(maths,science, color=colors)
plt.title('Scatter Plot')
plt.xlabel('Maths')
plt.ylabel('Science')
plt.show()
