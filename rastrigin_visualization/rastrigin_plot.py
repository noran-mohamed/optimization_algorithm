import matplotlib.pyplot as plt
import numpy as np

# Rastrigin function
def rastrigin(x, y, A=10):
    return A*2 + (x**2 - A*np.cos(2*np.pi*x)) + (y**2 - A*np.cos(2*np.pi*y))

# Generate grid
X = np.linspace(-5.12, 5.12, 200)
Y = np.linspace(-5.12, 5.12, 200)
X, Y = np.meshgrid(X, Y)
Z = rastrigin(X, Y)

# 3D surface plot
fig = plt.figure(figsize=(12,5))

ax = fig.add_subplot(1,2,1, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title("Rastrigin Function (Surface)")

# Contour plot
ax2 = fig.add_subplot(1,2,2)
contour = ax2.contourf(X, Y, Z, 50, cmap='viridis')
fig.colorbar(contour, ax=ax2)
ax2.set_title("Rastrigin Function (Contour)")

plt.show()
