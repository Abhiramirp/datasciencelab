from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

iris=load_iris()

x=iris.data
y=iris.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)

knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train,y_train)  #training
y_pred=knn.predict(x_test)

print("Accuracy : ",metrics.accuracy_score(y_test,y_pred))



print("Enter The Sample Data")

a=float(input("Enter Sepal Length In CM : "))
b=float(input("Enter Sepal width In CM : "))
c=float(input("Enter Petal Length In CM : "))
d=float(input("Enter Petal width In CM : "))

sample=[[a,b,c,d]]
pred=knn.predict(sample)
print(pred)

pred_v= iris.target_names[pred] 
print(pred_v)
