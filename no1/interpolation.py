import numpy as np
import matplotlib.pyplot as plt

c_x = [64.9074, 1.4811, -0.2601, 0.5949, 0.1263, -0.0090, -0.0052, -0.0006, -0.0000, -0.0000]
c_y = [40.0000, 2.5000, -5.3019e-15, 1.8693e-15, 1.3878e-15, 3.2632e-16, 3.9552e-17, 2.6599e-18, 9.4308e-20, 1.3768e-21]

def horner(c, t, t0=480, scale=30):
    z = (t - t0) / scale
    result = c[-1]

    for coef in reversed(c[:-1]):
        result = result * z + coef

    return result

t_values = np.arange(0, 541, 60)

px_values = [horner(c_x, t) for t in t_values]
py_values = [horner(c_y, t) for t in t_values]

print(px_values)
print(py_values)

colormap = plt.cm.coolwarm
colors = colormap(np.linspace(0, 1, len(t_values)))

plt.figure(figsize=(10, 6))
plt.plot(px_values, py_values, label="Interpolated Path", linestyle='-', color='b')

for i, (px, py, color) in enumerate(zip(px_values, py_values, colors)):
    plt.scatter(px, py, color=color, label=f"t = {t_values[i]}", zorder=5)

plt.xlabel("px(t)")
plt.ylabel("py(t)")
plt.title("Interpolation Using Horner's Method")
plt.grid(True)
plt.legend()
plt.show()

