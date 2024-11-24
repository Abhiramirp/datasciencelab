import numpy as np 
import matplotlib.pyplot as plt 
x=["Java","Python","Php","Javascript","c#","Cpp"] 
y=np.array([22.2,17.6,8.8,8,7.7,6.7]) 
plt.pie(y,labels=x,autopct='%2.2f%%') 
plt.title("Popularity of programming languages") 
plt.show() 
