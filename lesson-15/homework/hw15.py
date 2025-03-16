#q1
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return x**2 - 4*x + 4
x = np.linspace(-10, 10, 400)  
y = f(x)
plt.figure(figsize=(8, 5))
plt.plot(x, y, label=r'$f(x) = x^2 - 4x + 4$', color='b')
plt.xlabel('x-axis')
plt.ylabel('f(x)')
plt.title('Plot of $f(x) = x^2 - 4x + 4$')
plt.axhline(0, color='black', linewidth=1)  
plt.axvline(0, color='black', linewidth=1) 
plt.grid(True, linestyle='--', alpha=0.6)  
plt.legend()
plt.show()

#q2
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2 * np.pi, 400)  
sin_x = np.sin(x)
cos_x = np.cos(x)
plt.figure(figsize=(8, 5))
plt.plot(x, sin_x, linestyle='-', marker='o', color='r', label=r'$\sin(x)$')  
plt.plot(x, cos_x, linestyle='--', marker='s', color='b', label=r'$\cos(x)$')  
plt.xlabel('x-axis (radians)')
plt.ylabel('Function values')
plt.title(r'Plot of $\sin(x)$ and $\cos(x)$')
plt.axhline(0, color='black', linewidth=1)  
plt.axvline(0, color='black', linewidth=1) 
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], 
           ['0', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$'])  
plt.grid(True, linestyle='--', alpha=0.6)  
plt.legend()
plt.show()

#q3
import numpy as np
import matplotlib.pyplot as plt
x1 = np.linspace(-2, 2, 100)    
x2 = np.linspace(0, 2*np.pi, 100)  
x3 = np.linspace(-2, 2, 100)    
x4 = np.linspace(0, 5, 100)    
y1 = x1**3
y2 = np.sin(x2)
y3 = np.exp(x3)
y4 = np.log(x4 + 1)
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
axs[0, 0].plot(x1, y1, color='red')
axs[0, 0].set_title(r'$f(x) = x^3$')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('y')
axs[0, 0].grid(True)
axs[0, 1].plot(x2, y2, color='blue')
axs[0, 1].set_title(r'$f(x) = \sin(x)$')
axs[0, 1].set_xlabel('x')
axs[0, 1].set_ylabel('y')
axs[0, 1].grid(True)
axs[1, 0].plot(x3, y3, color='green')
axs[1, 0].set_title(r'$f(x) = e^x$')
axs[1, 0].set_xlabel('x')
axs[1, 0].set_ylabel('y')
axs[1, 0].grid(True)
axs[1, 1].plot(x4, y4, color='purple')
axs[1, 1].set_title(r'$f(x) = \log(x+1)$')
axs[1, 1].set_xlabel('x')
axs[1, 1].set_ylabel('y')
axs[1, 1].grid(True)
plt.tight_layout()
plt.show()

#q4
import numpy as np
import matplotlib.pyplot as plt
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)
colors = np.random.rand(100)  
plt.figure(figsize=(8, 6))
plt.scatter(x, y, c=colors, cmap='viridis', marker='o', edgecolors='black', alpha=0.75)
plt.title('Random Scatter Plot of 100 Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True, linestyle='--', alpha=0.6)
plt.colorbar(label='Color Intensity')  
plt.show()

#q5
import numpy as np
import matplotlib.pyplot as plt
data = np.random.normal(loc=0, scale=1, size=1000)
plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, color='royalblue', edgecolor='black', alpha=0.75)
plt.title('Histogram of Normally Distributed Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()

#q6
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.cos(X**2 + Y**2)
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
fig.colorbar(surf, shrink=0.6, aspect=10)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('f(x, y) = cos(x² + y²)')
ax.set_title('3D Surface Plot of f(x, y)')
plt.show()

#q7
import matplotlib.pyplot as plt
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]
colors = ['blue', 'green', 'red', 'purple', 'orange']
plt.figure(figsize=(8, 5))
plt.bar(products, sales, color=colors)
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Sales Data for Different Products")
plt.ylim(0, max(sales) + 50)  
plt.show()

#q8
import numpy as np
import matplotlib.pyplot as plt
time_periods = ['T1', 'T2', 'T3', 'T4']
category_A = [3, 5, 7, 6]
category_B = [4, 6, 5, 7]
category_C = [2, 3, 4, 5]
bar_width = 0.6
plt.figure(figsize=(8, 6))
plt.bar(time_periods, category_A, color='blue', label='Category A')
plt.bar(time_periods, category_B, bottom=category_A, color='green', label='Category B')
plt.bar(time_periods, category_C, bottom=np.array(category_A) + np.array(category_B), color='red', label='Category C')

plt.xlabel("Time Periods")
plt.ylabel("Contribution")
plt.title("Stacked Bar Chart of Category Contributions Over Time")
plt.legend()
plt.show()
