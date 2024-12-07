import csv

# Data
data = [
    {"y": 0, "xr": 317, "x_values": [0]},
    {"y": 413, "xr": 143, "x_values": [179, 488, 801, 1112, 1425, 1736]},
    {"y": 548, "xr": 88, "x_values": [109, 291, 483, 673, 863, 1052, 1243, 1435, 1627, 1813]},
    {"y": 608, "xr": 65, "x_values": [347, 483, 619, 755, 892, 1027, 1163, 1300, 1437, 1570]},
    {"y": 642, "xr": 50, "x_values": [484, 587, 693, 800, 905, 1013, 1220, 1226, 1333, 1435]},
    {"y": 660, "xr": 41, "x_values": [559, 649, 738, 828, 915, 1003, 1092, 1178, 1269, 1348]},
    {"y": 680, "xr": 35, "x_values": [631, 705, 772, 851, 924, 996, 1071, 1144, 1213, 1277]},
    {"y": 687, "xr": 29, "x_values": [675, 735, 801, 864, 928, 992, 1057, 1121, 1187, 1248]},
    {"y": 695, "xr": 27, "x_values": [701, 757, 817, 875, 932, 990, 1047, 1104, 1165, 1214]},
    {"y": 702, "xr": 25, "x_values": [729, 775, 826, 880, 938, 985, 1040, 1090, 1151, 1195]},
]

# Initialize results
dx_list = dict()
count = 0
for entry in data:
    xr = entry["xr"]
    x_values = [0] + entry["x_values"]  # Include the origin for each frame
    inner_list = []

    for i in range(1, len(x_values)):
        dx = (2.5 / xr) * (x_values[i] - x_values[i - 1])
        inner_list.append(dx)

    dx_list[f"t{count}"] = inner_list
    count += 1

# Calculate real x-values
res = dict()
for frame in dx_list:
    inner_list = []

    x_real_0 = round(dx_list[frame][0], 4)
    inner_list.append(x_real_0)
    for i in range(1, len(dx_list[frame])):
        x_real_i = dx_list[frame][i] + inner_list[i - 1]
        inner_list.append(round(x_real_i, 4))

    res[frame] = inner_list

# Generate CSV content
csv_file = "real_coordinates.csv"
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(["t", "real_x_values", "real_y_value"])

    # Write data rows
    t_values = [0, 60, 120, 180, 240, 300, 360, 420, 480, 540]  # Time frames
    y_values = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]  # Real y-values
    for i, (frame, x_values) in enumerate(res.items()):
        writer.writerow([t_values[i], ";".join(map(str, x_values)), y_values[i]])

print(f"Results saved to {csv_file}")

