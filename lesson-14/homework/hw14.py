#task1
import numpy as np
def fahrenheit_to_celsius(F):
    return (F - 32) * 5 / 9
vectorized_conversion = np.vectorize(fahrenheit_to_celsius)
F_temps = np.array([32, 68, 100, 212, 77])
C_temps = vectorized_conversion(F_temps)
print("Fahrenheit temperatures:", F_temps)
print("Celsius temperatures:", C_temps)

#task2
import numpy as np
def custom_power(base, exponent):
    return base ** exponent
vectorized_power = np.vectorize(custom_power)
bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])
results = vectorized_power(bases, exponents)
print("Base numbers:", bases)
print("Exponents:", exponents)
print("Results:", results)

#task3
import numpy as np
A = np.array([
    [4, 5, 6],
    [3, -1, 1],
    [2, 1, -2]
])
b = np.array([7, 4, 5])
solution = np.linalg.solve(A, b)
print("Solution (x, y, z):", solution)

#task4
import numpy as np
A = np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])
b = np.array([12, -5, 15])
solution = np.linalg.solve(A, b)
print("Solution (I1, I2, I3):", solution)

