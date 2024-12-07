import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Given data points (replace with your data)
t_actual = np.array([0, 60, 120, 180, 240, 300, 360, 420, 480, 540])  # Frame times
x = np.array([317, 143, 88, 65, 50, 41, 35, 29, 27, 25])              # x-coordinates
y = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45])                  # y-coordinates

# Perform cubic spline interpolation
spline_x = CubicSpline(t_actual, x, bc_type='natural')
spline_y = CubicSpline(t_actual, y, bc_type='natural')

# Evaluate at intervals of 1 frame and extrapolate to t=600
t_eval = np.arange(0, 601, 1)  # Interpolation and extrapolation range
x_interp = spline_x(t_eval)
y_interp = spline_y(t_eval)

# Extrapolated values at t=600
x_extrapolated = spline_x(600)
y_extrapolated = spline_y(600)

print(f"Extrapolated values at t=600: x = {x_extrapolated}, y = {y_extrapolated}")
print(f"Actual values at t=600: x = 2.336957, y = 50")
print(f"Differences: Δx = {abs(x_extrapolated - 2.336957)}, Δy = {abs(y_extrapolated - 50)}")

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t_eval, x_interp, label="Spline Interpolation for x(t)", color='blue')
plt.plot(t_eval, y_interp, label="Spline Interpolation for y(t)", color='green')
plt.scatter(t_actual, x, color='blue', label="x data points")
plt.scatter(t_actual, y, color='green', label="y data points")
plt.axvline(600, linestyle='--', color='red', label="Extrapolation point (t=600)")
plt.xlabel("Frames (t)")
plt.ylabel("Values")
plt.title("Cubic Spline Interpolation and Extrapolation")
plt.legend()
plt.grid()
plt.show()

from scipy.interpolate import PchipInterpolator


# Perform PCHIP interpolation
pch_x = PchipInterpolator(t_actual, x)
pch_y = PchipInterpolator(t_actual, y)

# Evaluate at intervals of 1 frame and extrapolate to t=600
x_interp_pchip = pch_x(t_eval)
y_interp_pchip = pch_y(t_eval)

x_extrapolated_pchip = pch_x(600)
y_extrapolated_pchip = pch_y(600)

print(f"PCHIP Extrapolated values at t=600: x = {x_extrapolated_pchip}, y = {y_extrapolated_pchip}")
print(f"Actual values at t=600: x = 2.336957, y = 50")
print(f"Differences: Δx = {abs(x_extrapolated_pchip - 2.336957)}, Δy = {abs(y_extrapolated_pchip - 50)}")

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t_eval, x_interp_pchip, label="PCHIP Interpolation for x(t)", color='blue')
plt.plot(t_eval, y_interp_pchip, label="PCHIP Interpolation for y(t)", color='green')
plt.scatter(t_actual, x, color='blue', label="x data points")
plt.scatter(t_actual, y, color='green', label="y data points")
plt.axvline(600, linestyle='--', color='red', label="Extrapolation point (t=600)")
plt.xlabel("Frames (t)")
plt.ylabel("Values")
plt.title("PCHIP Interpolation and Extrapolation")
plt.legend()
plt.grid()
plt.show()

