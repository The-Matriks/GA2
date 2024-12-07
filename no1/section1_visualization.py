import matplotlib.pyplot as plt

# Data provided by the user, each list inside represents different times (t = 0, 60, 120, etc.)
t_values = [0, 60, 120, 180, 240, 300, 360, 420, 480, 540]
real_x_values = [
    [0.0],
    [3.1293706293706296, 8.531468531468532, 14.003496503496503, 19.44055944055944, 24.912587412587413, 30.34965034965035],
    [3.096590909090909, 8.267045454545453, 13.721590909090907, 19.11931818181818, 24.517045454545453, 29.886363636363633, 35.3125, 40.76704545454545, 46.22159090909091, 51.50568181818181],
    [13.346153846153847, 18.576923076923077, 23.807692307692307, 29.038461538461537, 34.30769230769231, 39.5, 44.73076923076923, 50.0, 55.26923076923077, 60.38461538461538],
    [24.200000000000003, 29.35, 34.650000000000006, 40.00000000000001, 45.25000000000001, 50.650000000000006, 61.00000000000001, 61.300000000000004, 66.65, 71.75],
    [34.08536585365854, 39.573170731707314, 45.0, 50.48780487804878, 55.792682926829265, 61.15853658536585, 66.58536585365853, 71.82926829268293, 77.3780487804878, 82.1951219512195],
    [45.07142857142857, 50.357142857142854, 55.14285714285714, 60.78571428571428, 65.99999999999999, 71.14285714285712, 76.49999999999999, 81.7142857142857, 86.64285714285712, 91.2142857142857],
    [58.189655172413794, 63.36206896551724, 69.05172413793103, 74.48275862068965, 80.0, 85.51724137931035, 91.12068965517241, 96.63793103448276, 102.32758620689656, 107.58620689655173],
    [64.9074074074074, 70.0925925925926, 75.64814814814815, 81.01851851851852, 86.29629629629629, 91.66666666666666, 96.94444444444443, 102.2222222222222, 107.87037037037035, 112.40740740740739],
    [72.9, 77.5, 82.6, 88.0, 93.8, 98.5, 104.0, 109.0, 115.1, 119.5]
]
real_y_values = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]

# Create the plot
plt.figure(figsize=(10, 8))
for i, x_vals in enumerate(real_x_values):
    plt.scatter(x_vals, [real_y_values[i]]*len(x_vals), label=f't={t_values[i]}s')

plt.xlabel('Real X Values (meters)')
plt.ylabel('Real Y Values (meters)')
plt.title('Visualization of the Self-Driving Car\'s Track Navigation')
plt.legend(title="Time Frames")
plt.grid(True)
plt.show()