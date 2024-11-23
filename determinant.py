import numpy as np
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))


matrix = []


for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element for position ({i}, {j}): "))
        row.append(element)
    matrix.append(row)


print("The matrix is:")
for row in matrix:
    print(row)
det = np.linalg.det(matrix) 
print("\nDeterminant of given matrix:") 
print(int(det)) 
