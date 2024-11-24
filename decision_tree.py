import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

# Load Iris dataset from CSV
iris = pd.read_csv('iris.csv')

# Split features and target
x = iris.iloc[:, :-1].values  # All columns except the last one (features)
y = iris.iloc[:, -1]          # Last column (target)

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

# Train Decision Tree Classifier
dt = DecisionTreeClassifier()
dt.fit(x_train, y_train)

# Predict on test data
y_pred = dt.predict(x_test)

# Calculate accuracy
print("Accuracy: ", metrics.accuracy_score(y_test, y_pred))

# Predict a single sample
print("\nEnter The Sample Data:")
a = float(input("Enter Sepal Length in CM: "))
b = float(input("Enter Sepal Width in CM: "))
c = float(input("Enter Petal Length in CM: "))
d = float(input("Enter Petal Width in CM: "))

sample = [[a, b, c, d]]
pred = dt.predict(sample)
print("Prediction for the given sample: ", pred)



# Visualization
import matplotlib.pyplot as plt
from sklearn import tree

plt.figure(figsize=(12, 12))

# Replace feature and class names with actual values
feature_names = iris.columns[:-1]  # Feature names are all columns except the last one
class_names = iris[y.name].unique()  # Unique target names from the target column

tree.plot_tree(dt,  filled=True,feature_names=feature_names, class_names=class_names)
plt.title("Decision Tree Visualization")
plt.show()
