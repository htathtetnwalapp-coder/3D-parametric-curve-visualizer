import numpy as np
import matplotlib.pyplot as plt

# Ask user for equations
x_expr = input("Enter x(t): ")
y_expr = input("Enter y(t): ")
z_expr = input("Enter z(t): ")

t = np.linspace(0, 10, 200)

# Convert string → actual math
x = eval(x_expr)
y = eval(y_expr)
z = eval(z_expr)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Color changes along the curve
color = np.linspace(0, 1, len(t))

for i in range(len(t)-1):
    ax.plot(x[i:i+2], y[i:i+2], z[i:i+2], color=plt.cm.viridis(color[i]))

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

ax.set_title("3D Curve (Colored by Time)")

plt.show() 