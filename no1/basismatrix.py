import numpy as np

# Given data points (replace with your processed data)
t = np.array([0, 60, 120, 180, 240, 300, 360, 420, 480, 540])  # Time data
x = np.array([317, 143, 88, 65, 50, 41, 35, 29, 27, 25])       # X-coordinates
y = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45])           # Y-coordinates

# Basis functions
def construct_matrix(t, basis_type):
    n = len(t)
    A = np.zeros((n, n))
    if basis_type == 'A':  # Phi_i(t) = t^i
        for i in range(n):
            for j in range(n):
                A[i, j] = t[i] ** j
    elif basis_type == 'B':  # Phi_i(t) = (t - 60)^i
        for i in range(n):
            for j in range(n):
                A[i, j] = (t[i] - 60) ** j
    elif basis_type == 'C':  # Phi_i(t) = (t - 480)^i
        for i in range(n):
            for j in range(n):
                A[i, j] = (t[i] - 480) ** j
    elif basis_type == 'D':  # Phi_i(t) = ((t - 480)/30)^i
        for i in range(n):
            for j in range(n):
                A[i, j] = ((t[i] - 480) / 30) ** j
    return A

# Compute condition number
def compute_condition_number(A):
    norm_A = np.linalg.norm(A, 2)        # Spectral norm of A
    norm_A_inv = np.linalg.norm(np.linalg.inv(A), 2)  # Spectral norm of A^-1
    return norm_A * norm_A_inv

# Solve linear systems and compute condition numbers for each basis
bases = ['A', 'B', 'C', 'D']
results = {}

for basis in bases:
    A = construct_matrix(t, basis)
    condition_number = compute_condition_number(A)
    results[basis] = condition_number
    # Solve Ac = x and Ac = y
    c_x = np.linalg.solve(A, x)
    c_y = np.linalg.solve(A, y)
    print(f"Basis {basis} - Condition number: {condition_number}")
    print(f"Coefficients for x: {c_x}")
    print(f"Coefficients for y: {c_y}")

# Sort and display condition numbers
sorted_results = sorted(results.items(), key=lambda x: x[1])
print("\nCondition numbers (sorted from best to worst):")
for basis, cond_num in sorted_results:
    print(f"Basis {basis}: {cond_num}")
