import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([1,2,6])
ypoints=np.array([3,10,12])
apoints=np.array([3,7,12])
bpoints=np.array([6,10,17])

plt.plot(apoints,bpoints,'g',label="student")
plt.plot(xpoints,ypoints,'r',label="teacher")

plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend()
plt.title("STUDENT TEACHER PERFORMANCE GRAPH")
plt.show()
