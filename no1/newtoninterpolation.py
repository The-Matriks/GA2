import numpy as np
import matplotlib.pyplot as plt

# Given data points
t = np.array([0, 60, 120, 180, 240, 300, 360, 420, 480, 540])  # Time data
x = np.array([0.0, 3.129, 3.097, 13.346, 24.2, 34.085, 45.071, 58.19, 64.907, 72.9])  # Selected x-coordinates
y = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45])  # Y-coordinates
# Divided Differences Algorithm
def divided_differences(t, values):
    n = len(t)
    table = np.zeros((n, n))
    table[:, 0] = values  # First column is the values themselves

    for j in range(1, n):
        for i in range(n - j):
            table[i, j] = (table[i + 1, j - 1] - table[i, j - 1]) / (t[i + j] - t[i])
    return table[0, :]  # Return the coefficients (top row)

# Newton Polynomial Evaluation
def newton_polynomial(t_eval, t, coeffs):
    n = len(coeffs)
    result = 0
    for i in range(n - 1, -1, -1):  # Use Horner's method for efficiency
        result = coeffs[i] + (t_eval - t[i]) * result
    return result

# Compute Newton coefficients for x(t) and y(t)
coeff_x = divided_differences(t, x)
coeff_y = divided_differences(t, y)

# Extend to p10(t) with t=600
t_extended = np.append(t, 600)
x_extended = np.append(x, 2.336957)  # Actual x(600)
y_extended = np.append(y, 50.0)  # Actual y(600)
coeff_x_extended = divided_differences(t_extended, x_extended)
coeff_y_extended = divided_differences(t_extended, y_extended)

# Evaluate p9(t) and p10(t)
t_eval = np.linspace(0, 600, 601)
p9_x = [newton_polynomial(ti, t, coeff_x) for ti in t_eval]
p9_y = [newton_polynomial(ti, t, coeff_y) for ti in t_eval]
p10_x = [newton_polynomial(ti, t_extended, coeff_x_extended) for ti in t_eval]
p10_y = [newton_polynomial(ti, t_extended, coeff_y_extended) for ti in t_eval]

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(t_eval, p9_x, label="p9_x(t)", color="blue", linestyle="--")
plt.plot(t_eval, p10_x, label="p10_x(t)", color="blue")
plt.plot(t_eval, p9_y, label="p9_y(t)", color="green", linestyle="--")
plt.plot(t_eval, p10_y, label="p10_y(t)", color="green")
plt.scatter(t, x, color="blue", label="x interpolation points")
plt.scatter(t, y, color="green", label="y interpolation points")
plt.axvline(600, color="red", linestyle="--", label="Extrapolation at t=600")
plt.xlabel("Time (t)")
plt.ylabel("Values")
plt.title("Newton Form of p9(t) and p10(t)")
plt.legend()
plt.grid()
plt.show()
