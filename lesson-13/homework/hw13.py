#q1
import numpy as np
vector = np.arange(10, 50)
print(vector)

#q2
import numpy as np
matrix = np.arange(9).reshape(3, 3)
print(matrix)

#q3
import numpy as np
identity_matrix = np.eye(3)
print(identity_matrix)

#q4
import numpy as np
random_array = np.random.rand(3, 3, 3)
print(random_array)

#q5
import numpy as np
random_array = np.random.rand(10, 10)
min_value = np.min(random_array)
max_value = np.max(random_array)
print("Random 10x10 Array:\n", random_array)
print("\nMinimum Value:", min_value)
print("Maximum Value:", max_value)

#q6
import numpy as np
random_vector = np.random.rand(30)
mean_value = np.mean(random_vector)
print("Random Vector:\n", random_vector)
print("\nMean Value:", mean_value)

#q7
import numpy as np
random_matrix = np.random.rand(5, 5)
min_val = np.min(random_matrix)
max_val = np.max(random_matrix)
normalized_matrix = (random_matrix - min_val) / (max_val - min_val)
print("Original 5x5 Random Matrix:\n", random_matrix)
print("\nNormalized Matrix:\n", normalized_matrix)

#q8
import numpy as np
A = np.random.rand(5, 3)
B = np.random.rand(3, 2)
result = np.dot(A, B)  
print("Matrix A (5x3):\n", A)
print("\nMatrix B (3x2):\n", B)
print("\nResultant Matrix (5x2):\n", result)

#q9
import numpy as np
A = np.random.rand(3, 3)
B = np.random.rand(3, 3)
dot_product = np.dot(A, B)  
print("Matrix A:\n", A)
print("\nMatrix B:\n", B)
print("\nDot Product (A · B):\n", dot_product)

#q10
import numpy as np
matrix = np.random.rand(4, 4)
transpose_matrix = matrix.T  
print("Original 4x4 Matrix:\n", matrix)
print("\nTranspose of the Matrix:\n", transpose_matrix)

#q11
import numpy as np
matrix = np.random.rand(3, 3)
determinant = np.linalg.det(matrix)
print("3x3 Matrix:\n", matrix)
print("\nDeterminant of the Matrix:", determinant)

#q12
import numpy as np
A = np.random.rand(3, 4)
B = np.random.rand(4, 3)
product = np.dot(A, B)  
print("Matrix A (3x4):\n", A)
print("\nMatrix B (4x3):\n", B)
print("\nMatrix Product (A · B) (3x3):\n", product)

#q13
import numpy as np
A = np.random.rand(3, 3)
v = np.random.rand(3, 1)  
result = np.dot(A, v)  
print("Matrix A (3x3):\n", A)
print("\nColumn Vector v (3x1):\n", v)
print("\nMatrix-Vector Product (A · v):\n", result)

#q14
import numpy as np
A = np.random.rand(3, 3)
b = np.random.rand(3, 1)
x = np.linalg.solve(A, b)
print("Matrix A (3x3):\n", A)
print("\nColumn Vector b (3x1):\n", b)
print("\nSolution x (3x1):\n", x)

#q15
import numpy as np
matrix = np.random.rand(5, 5)
row_sums = np.sum(matrix, axis=1)
col_sums = np.sum(matrix, axis=0)
print("5x5 Matrix:\n", matrix)
print("\nRow-wise Sums:\n", row_sums)
print("\nColumn-wise Sums:\n", col_sums)
