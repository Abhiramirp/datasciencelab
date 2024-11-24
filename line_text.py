import matplotlib.pyplot as plt
x=[]
y=[]
f=open("TextLine.txt")
next(f)
for row in f:
	row=row.split('	')
	x.append(int(row[0]))
	y.append(int(row[1]))
plt.xlabel("x-axis")
plt.ylabel("y-axis")	
plt.plot(x,y)
plt.show()	
