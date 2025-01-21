# This code is to generate a straight line on a graph using Python and matplotlib.

import matplotlib.pyplot as plt
import numpy as np

# Define the slope (m) and y-intercept (b)
m = 2  # Slope
b = 1  # Y-intercept

# Generate x values
x = np.linspace(-10, 10, 100)  # 100 points between -10 and 10

# Calculate y values
y = m * x + b

# Plot the line
plt.plot(x, y, label=f"y = {m}x + {b}")

# Add labels, title, and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of y = mx + b')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # X-axis
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # Y-axis
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
