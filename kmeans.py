import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

iris = pd.read_csv('iris.csv')

x = iris.iloc[:,:-1].values

# Set n_clusters to 3 since the Iris dataset has 3 species
kmeans = KMeans(n_clusters=3, init='k-means++', random_state=42, n_init=10)
kmeans.fit(x)

centroids = kmeans.cluster_centers_

print("Centroids for Cluster 1:")
print(centroids[0])
print("Centroids for Cluster 2:")
print(centroids[1])
print("Centroids for Cluster 3:")
print(centroids[2])

print("Enter the sample data")

a = float(input("Enter sepal length in cm: "))
b = float(input("Enter sepal width in cm: "))
c = float(input("Enter petal length in cm: "))
d = float(input("Enter petal width in cm: "))

sample = np.array([[a, b, c, d]])
pred= kmeans.predict(sample)
print("The input belongs to Cluster:", pred[0]+1)
