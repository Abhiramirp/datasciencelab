import matplotlib.pyplot as plt;

diction = {'Java':22.2,'Python':17.6,'PHP':8.8,'JavaScript':8,'C##':7.7,'C++':6.7}
lang = list(diction.keys())
val = list(diction.values())
plt.bar(lang,val, color='red')
plt.ylabel('Popularity')
plt.title('Programming language usage')
plt.show()
