import os
import csv
import time
import matplotlib.pyplot as plt
from logloss import log_loss_y1, log_loss_y0
from simpsonmethod import composite_simpson
from adaptivequadrature import adaptive_quadrature
from romberg import romberg_integration

# Define the integration range
a, b = 0, 10
tolerance = 1e-4  # For adaptive quadrature
N_values = [10, 50, 100, 500, 1000]  # Subdivisions for Composite Simpson
m_values = [4, 6, 7, 9, 10]  # Levels for Romberg Integration

def run_composite_simpson(log_loss, label="y=1"):
    print(f"\nComposite Simpson's Rule Results for {label}:")
    print(f"{'N (Subdivisions)':<20}{'Result':<15}{'Time (s)':<10}")
    print("-" * 45)
    results = []
    times = []
    for N in N_values:
        start = time.perf_counter()
        result = composite_simpson(log_loss, a, b, N)
        end = time.perf_counter()
        results.append(result)
        times.append(end - start)
        print(f"{N:<20}{result:<15.6f}{(end - start):.8f}")
    return results, times

def run_adaptive_quadrature(log_loss, label="y=1"):
    print(f"\nAdaptive Quadrature Results for {label}:")
    print(f"{'Tolerance':<15}{'Result':<15}{'Time (s)':<10}")
    print("-" * 40)
    start = time.perf_counter()
    result = adaptive_quadrature(log_loss, a, b, tol=tolerance)
    end = time.perf_counter()
    computation_time = end - start
    print(f"{tolerance:<15}{result:<15.6f}{computation_time:.8f}")
    return result, computation_time

def run_romberg_experiments(log_loss, label="y=1"):
    print(f"\nRomberg Integration Results for {label}:")
    print(f"{'m (Levels)':<12}{'N (Subdivisions)':<20}{'Result':<15}{'Time (s)':<10}")
    print("-" * 55)
    results = []
    times = []
    for m in m_values:
        start = time.perf_counter()
        result = romberg_integration(log_loss, a, b, max_levels=m)
        end = time.perf_counter()
        
        # Number of subdivisions is 2^(m-1)
        N = 2**(m - 1)
        computation_time = end - start

        results.append(result)
        times.append(computation_time)
        print(f"{m:<12}{N:<20}{result:<15.6f}{computation_time:.8f}")
    return results, times

def visualize_results(y1_simpson, y1_times, y1_adaptive, y1_adaptive_time, y1_romberg, y1_romberg_times,
                               y0_simpson, y0_times, y0_adaptive, y0_adaptive_time, y0_romberg, y0_romberg_times):
    # Visualization for y=1
    plt.figure(figsize=(15, 8))

    # Accuracy Plot for y=1
    plt.subplot(2, 1, 1)
    plt.plot(N_values, y1_simpson, marker='o', label="Composite Simpson")
    plt.axhline(y1_adaptive, color='g', linestyle='--', label="Adaptive Quadrature")
    plt.plot(m_values, y1_romberg, marker='s', label="Romberg Integration")
    plt.xlabel("Subdivisions (N) / Levels (m)")
    plt.ylabel("Integral Value")
    plt.title("Integral Results Comparison (y=1)")
    plt.legend()
    plt.grid()

    # Computation Time Plot for y=1
    plt.subplot(2, 1, 2)
    plt.plot(N_values, y1_times, marker='o', label="Composite Simpson")
    plt.bar(["Adaptive Quadrature"], [y1_adaptive_time], color='g', label="Adaptive Quadrature")
    plt.plot(m_values, y1_romberg_times, marker='s', label="Romberg Integration")
    plt.xlabel("Subdivisions (N) / Levels (m)")
    plt.ylabel("Computation Time (seconds)")
    plt.title("Computation Time Comparison (y=1)")
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.show()

    # Visualization for y=0
    plt.figure(figsize=(15, 8))

    # Accuracy Plot for y=0
    plt.subplot(2, 1, 1)
    plt.plot(N_values, y0_simpson, marker='o', label="Composite Simpson")
    plt.axhline(y0_adaptive, color='r', linestyle='--', label="Adaptive Quadrature")
    plt.plot(m_values, y0_romberg, marker='s', label="Romberg Integration")
    plt.xlabel("Subdivisions (N) / Levels (m)")
    plt.ylabel("Integral Value")
    plt.title("Integral Results Comparison (y=0)")
    plt.legend()
    plt.grid()

    # Computation Time Plot for y=0
    plt.subplot(2, 1, 2)
    plt.plot(N_values, y0_times, marker='o', label="Composite Simpson")
    plt.bar(["Adaptive Quadrature"], [y0_adaptive_time], color='r', label="Adaptive Quadrature")
    plt.plot(m_values, y0_romberg_times, marker='s', label="Romberg Integration")
    plt.xlabel("Subdivisions (N) / Levels (m)")
    plt.ylabel("Computation Time (seconds)")
    plt.title("Computation Time Comparison (y=0)")
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.show()

def save_results_to_csv(directory, filename, headers, rows):
    # Ensure the output directory exists
    os.makedirs(directory, exist_ok=True)

    # Write results to CSV
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"Results saved to {filepath}")

if __name__ == "__main__":
    # Run Composite Simpson
    simpson_results, simpson_times = run_composite_simpson(log_loss_y1, "y=1")
    simpson_results_y0, simpson_times_y0 = run_composite_simpson(log_loss_y0, "y=0")

    # Run Adaptive Quadrature
    adaptive_result, adaptive_time = run_adaptive_quadrature(log_loss_y1, "y=1")
    adaptive_result_y0, adaptive_time_y0 = run_adaptive_quadrature(log_loss_y0, "y=0")

    # Run Romberg Integration
    romberg_results, romberg_times = run_romberg_experiments(log_loss_y1, "y=1")
    romberg_results_y0, romberg_times_y0 = run_romberg_experiments(log_loss_y0, "y=0")

    # Visualize All Results
    visualize_results(
        simpson_results, simpson_times, adaptive_result, adaptive_time, romberg_results, romberg_times,
        simpson_results_y0, simpson_times_y0, adaptive_result_y0, adaptive_time_y0, romberg_results_y0, romberg_times_y0
    )

    # Save results to CSV
    output_dir = "output_no2"
    save_results_to_csv(
        output_dir,
        "composite_simpson.csv",
        ["N (Subdivisions)", "Result (y=1)", "Time (s) (y=1)", "Result (y=0)", "Time (s) (y=0)"],
        [[N, r1, t1, r0, t0] for N, r1, t1, r0, t0 in zip(N_values, simpson_results, simpson_times, simpson_results_y0, simpson_times_y0)]
    )
    save_results_to_csv(
        output_dir,
        "adaptive_quadrature.csv",
        ["Tolerance", "Result (y=1)", "Time (s) (y=1)", "Result (y=0)", "Time (s) (y=0)"],
        [[tolerance, adaptive_result, adaptive_time, adaptive_result_y0, adaptive_time_y0]]
    )
    save_results_to_csv(
        output_dir,
        "romberg_integration.csv",
        ["m (Levels)", "N (Subdivisions)", "Result (y=1)", "Time (s) (y=1)", "Result (y=0)", "Time (s) (y=0)"],
        [[m, 2**(m - 1), r1, t1, r0, t0] for m, r1, t1, r0, t0 in zip(m_values, romberg_results, romberg_times, romberg_results_y0, romberg_times_y0)]
    )
