import numpy as np
import matplotlib.pyplot as plt

# Logistic growth equation
def g(p, r, k):
    return p + r * p * (1 - p / k)

# Initial parameters
p0 = np.float64(10)  # Initial population
r = 0.2  # Growth rate
k = 100  # Carrying capacity
tolerance = 1.0e-4  # Convergence criterion
NO = 1000  # Maximum iterations

# Lists to store iterations for plotting
iterations = [p0]
population_values = [p0]

i = 1
while i <= NO:
    p = g(p0, r, k)
    population_values.append(p)
    iterations.append(i)
    
    if np.abs(p - p0) < tolerance:
        break
    
    print(f"{i}th iteration: Population = {p:.6f}")
    
    i += 1
    p0 = p

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(iterations, population_values, marker='o', linestyle='-', color='b', label="Population Growth")

# Highlight the converged population value
plt.axhline(population_values[-1], color='r', linestyle='--', label=f"Converged Value: {population_values[-1]:.2f}")

# Labels and title
plt.title("Fixed-Point Iteration for Population Growth (Logistic Model)")
plt.xlabel("Iteration Number")
plt.ylabel("Population")
plt.legend()
plt.grid(True, linestyle="--", linewidth=0.5)

# Show the plot
plt.show()

# Print final result
if i > NO:
    print("The method failed after NO iterations")
else:
    print(f"The method is successful. Converged population: {population_values[-1]:.6f}")
