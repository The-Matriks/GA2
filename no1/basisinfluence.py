import numpy as np

# Given data points (replace with your processed data from Section 1)
t = np.array([0, 60, 120, 180, 240, 300, 360, 420, 480, 540])  # Example time data
x = np.array([317, 143, 88, 65, 50, 41, 35, 29, 27, 25])       # Replace with your x data
y = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45])           # Replace with your y data

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

# Main computations
bases = ['A', 'B', 'C', 'D']
results = {}

for basis in bases:
    A = construct_matrix(t, basis)
    condition_number = compute_condition_number(A)
    results[basis] = condition_number
    print(f"Condition number for Basis {basis}: {condition_number}")

# Optional: Compare condition numbers
sorted_results = sorted(results.items(), key=lambda x: x[1])
print("\nCondition numbers (sorted from best to worst):")
for basis, cond_num in sorted_results:
    print(f"Basis {basis}: {cond_num}")
