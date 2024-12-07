import numpy as np
import matplotlib.pyplot as plt

# Coefficients for Basis D
c_x = [64.9074, 1.4811, -0.2601, 0.5949, 0.1263, -0.0090, -0.0052, -0.0006, -0.0000, -0.0000]
c_y = [40.0000, 2.5000, -5.3019e-15, 1.8693e-15, 1.3878e-15, 3.2632e-16, 3.9552e-17, 2.6599e-18, 9.4308e-20, 1.3768e-21]

# Function to evaluate p_9(t) using Horner's method
def horner(coeffs, t):
    result = 0
    for coeff in reversed(coeffs):
        result = result * t + coeff
    return result

# Define t_actual and scale to Basis D's domain
t_actual = np.linspace(0, 600, 601)
t_scaled = (t_actual - 480) / 30

# Evaluate p_9(t) for x and y
p_x = [horner(c_x, t) for t in t_scaled]
p_y = [horner(c_y, t) for t in t_scaled]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(t_actual, p_x, label="p_x(t)", color='blue')
plt.plot(t_actual, p_y, label="p_y(t)", color='green')
plt.scatter(np.linspace(0, 540, 10), [27, 25, 29, 35, 41, 50, 65, 88, 143, 317], color='blue', marker='o', label="x interpolation points")
plt.scatter(np.linspace(0, 540, 10), [0, 5, 10, 15, 20, 25, 30, 35, 40, 45], color='green', marker='o', label="y interpolation points")
plt.axvline(600, linestyle='--', color='red', label="Extrapolation at t=600")
plt.xlabel("Frames (t)")
plt.ylabel("Polynomial Values")
plt.title("Horner's Method: Polynomial Interpolation using Basis D")
plt.legend()
plt.grid()
plt.show()
