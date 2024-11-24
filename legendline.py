import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,6])
y=np.array([3,10,12])
a=np.array([3,7,12])
b=np.array([6,10,17])

plt.plot(a,b,'g',label="student")
plt.plot(x,y,'r',label="teacher")

plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend()
plt.title("STUDENT TEACHER PERFORMANCE GRAPH")
plt.show()
