import numpy as np
import matplotlib.pyplot as plt

# Define the x values from -2π to 2π
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)  # 1000 points in that range
# Calculate the sine of x
y = np.sin(x)

# Create the plot
plt.figure(figsize=(10, 5))  # Set the figure size
plt.plot(x, y, label='sin(x)', color='blue')  # Plot the sine wave
plt.title('Sine Wave')
plt.xlabel('x (radians)')
plt.ylabel('sin(x)')
plt.axhline(0, color='black', lw=0.5, ls='--')  # Add x-axis
plt.axvline(0, color='black', lw=0.5, ls='--')  # Add y-axis
plt.grid()  # Add grid
plt.legend()  # Add legend

# Save the plot as a PNG file
plt.savefig('sine_wave.png')

# Optionally, display the plot
plt.show()