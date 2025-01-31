import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x) based on the equation 2x^3 - 2x - 5 = 0
def f(x):
    return 2 * x**3 - 2 * x - 5

# Define the fixed-point iteration function Phi(x)
def phi(x):
    return ((2 * x + 5) / 2) ** (1 / 3)

# Perform the fixed-point iteration
def fixed_point_iteration(x0, tol=1e-6, maxiter=100):
    iterations = [x0]  # Store the iterations
    for _ in range(maxiter):
        x_next = phi(iterations[-1])
        iterations.append(x_next)
        if abs(x_next - iterations[-2]) < tol:
            break
    return iterations

# Initial guess
x0 = 1.5
iterations = fixed_point_iteration(x0)

# Generate x values for the plot
x = np.linspace(1, 2, 500)  # Range based on the fixed interval

# Calculate corresponding y values
y = f(x)

# Create the plot
plt.figure(figsize=(12, 8))

# Plot the original function
plt.plot(x, y, label=r"$2x^3 - 2x - 5 = 0$", color='blue')

# Highlight the x-axis and y-axis
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # x-axis
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # y-axis

# Plot the iterative points
for i, x_val in enumerate(iterations[:-1]):
    x_next = iterations[i + 1]
    plt.plot([x_val, x_val], [0, f(x_val)], color='green', linestyle='--', linewidth=0.8)  # Vertical line
    plt.plot([x_val, x_next], [f(x_val), 0], color='red', linestyle='--', linewidth=0.8)  # Horizontal line

# Mark the iterations
plt.scatter(iterations, [0] * len(iterations), color='purple', zorder=5, label='Iterations')

# Add annotations for clarity
plt.title("Fixed-Point Iteration for $2x^3 - 2x - 5 = 0$", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("f(x)", fontsize=12)

# Add grid and legend
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend(fontsize=12)

# Show the plot
plt.show()

# Print the iterations and the approximate root
print("Iterations:")
for i, x_val in enumerate(iterations):
    print(f"x_{i} = {x_val:.6f}")

print(f"\nApproximate root: x = {iterations[-1]:.6f}")
