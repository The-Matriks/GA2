import numpy as np

def cubic_spline(t, y):
    n = len(t) - 1  # Number of intervals
    h = np.diff(t)  # Interval widths

    # Set up the system of equations for the second derivatives (M)
    A = np.zeros((n + 1, n + 1))
    rhs = np.zeros(n + 1)

    # Natural spline boundary conditions
    A[0, 0] = 1  # S''(t_0) = 0
    A[n, n] = 1  # S''(t_n) = 0

    # Fill the system of equations
    for i in range(1, n):
        A[i, i - 1] = h[i - 1]  # Lower diagonal
        A[i, i] = 2 * (h[i - 1] + h[i])  # Main diagonal
        A[i, i + 1] = h[i]  # Upper diagonal
        rhs[i] = (3 / h[i]) * (y[i + 1] - y[i]) - (3 / h[i - 1]) * (y[i] - y[i - 1])

    # Solve for second derivatives (M)
    M = np.linalg.solve(A, rhs)

    # Compute coefficients a, b, c, d for each interval
    a = y[:-1]
    b = np.zeros(n)
    c = M[:-1] / 2
    d = np.zeros(n)

    for i in range(n):
        b[i] = ((y[i + 1] - y[i]) / h[i]) - (h[i] * (M[i + 1] + 2 * M[i]) / 3)
        d[i] = (M[i + 1] - M[i]) / (3 * h[i])

    # Return coefficients and helper function for evaluation
    return a, b, c, d, t

def evaluate_spline(t_eval, a, b, c, d, t):
    # Find the interval for t_eval
    idx = np.searchsorted(t, t_eval) - 1
    idx = np.clip(idx, 0, len(a) - 1)

    # Compute the spline value
    dx = t_eval - t[idx]
    return a[idx] + b[idx] * dx + c[idx] * dx**2 + d[idx] * dx**3
