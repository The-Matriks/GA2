import numpy as np
import matplotlib.pyplot as plt

# Coefficients for best basis
c_x = [64.9074, 1.4811, -0.2601, 0.5949, 0.1263, -0.0090, -0.0052, -0.0006, -0.0000, -0.0000]
c_y = [40.0000, 2.5000, -5.3019e-15, 1.8693e-15, 1.3878e-15, 3.2632e-16, 3.9552e-17, 2.6599e-18, 9.4308e-20, 1.3768e-21]

# Horner's Method for nested polynomial evaluation
def horner(c, t, t0=480, scale=30):
    z = (t - t0) / scale
    result = c[-1]
    for coef in reversed(c[:-1]):
        result = result * z + coef
    return result

# Time values
t_values = np.arange(0, 601, 60)  # Interpolating up to t=600

# Interpolated x and y values
px_values = [horner(c_x, t) for t in t_values]
py_values = [horner(c_y, t) for t in t_values]

# Extrapolated value comparison
extrapolated_x, extrapolated_y = horner(c_x, 600), horner(c_y, 600)
actual_x, actual_y = 2.336957, 50
error_x = actual_x - extrapolated_x
error_y = actual_y - extrapolated_y

print(f"Extrapolated at t=600: (x, y) = ({extrapolated_x}, {extrapolated_y})")
print(f"Actual at t=600: (x, y) = ({actual_x}, {actual_y})")
print(f"Errors: Δx = {error_x}, Δy = {error_y}")

# Visualization
colormap = plt.cm.coolwarm
colors = colormap(np.linspace(0, 1, len(t_values)))

plt.figure(figsize=(10, 6))
plt.plot(px_values, py_values, label="Interpolated Path", linestyle='-', color='b')
plt.scatter(actual_x, actual_y, color="red", label="Actual Point at t=600", zorder=5)

for i, (px, py, color) in enumerate(zip(px_values, py_values, colors)):
    plt.scatter(px, py, color=color, label=f"t = {t_values[i]}", zorder=5)

plt.xlabel("px(t) (meters)")
plt.ylabel("py(t) (meters)")
plt.title("Interpolation Using Horner's Method")
plt.grid(True)
plt.legend()
plt.show()
