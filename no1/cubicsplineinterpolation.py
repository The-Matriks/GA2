import numpy as np
import matplotlib.pyplot as plt
from cubicspline import cubic_spline, evaluate_spline

# Given data points
t = np.array([0, 60, 120, 180, 240, 300, 360, 420, 480, 540])  # Time data
x = np.array([0.0, 3.129, 3.097, 13.346, 24.2, 34.085, 45.071, 58.19, 64.907, 72.9])  # Selected x-coordinates
y = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45])  # Y-coordinates

# Compute cubic spline coefficients
a_x, b_x, c_x, d_x, t_x = cubic_spline(t, x)
a_y, b_y, c_y, d_y, t_y = cubic_spline(t, y)

# Evaluate spline
t_eval = np.linspace(0, 540, 600)
spline_x_vals = [evaluate_spline(te, a_x, b_x, c_x, d_x, t_x) for te in t_eval]
spline_y_vals = [evaluate_spline(te, a_y, b_y, c_y, d_y, t_y) for te in t_eval]

print(spline_x_vals)
print(spline_y_vals)

# Plot the parametric cubic spline
plt.figure(figsize=(10, 6))
plt.plot(spline_x_vals, spline_y_vals, label="Parametric Spline (x, y)", color="orange")
plt.scatter(x, y, color="blue", label="Data Points (x, y)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Parametric Cubic Spline Interpolation")
plt.legend()
plt.grid()
plt.show()
# Plot results
