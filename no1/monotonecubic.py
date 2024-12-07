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
