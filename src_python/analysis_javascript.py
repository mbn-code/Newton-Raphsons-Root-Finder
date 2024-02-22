import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the Excel file
df = pd.read_excel('../benchmark_data_javascript.xlsx')

# Calculate the average time for each function and initial guess
average_times = df.groupby(['Function', 'Initial Guess'])['Time'].mean()

# Calculate the overall average time
overall_average_time = df['Time'].mean()

# Print the average times
print('Average times:')
print(average_times)
print('\nOverall average time:', overall_average_time)

# Generate a color palette for the bar chart
colors = plt.cm.viridis(np.linspace(0, 1, len(average_times)))

# Plot a bar chart of the average execution times
average_times.plot(kind='bar', color=colors, edgecolor='black', title='Average Execution Time per Function and Initial Guess')

# Add gridlines
plt.grid(True, linestyle='--', alpha=0.6)

# Add the overall average time as a horizontal line
plt.axhline(overall_average_time, color='red', linestyle='--', label='Overall Average')
plt.legend()

# Plot the initial guess for each function
initial_guesses = df.groupby('Function')['Initial Guess'].unique()

# Show the plots
plt.show()

# Find the functions with the shortest and longest execution times
min_time_function = average_times.idxmin()
max_time_function = average_times.idxmax()

print(f"The fastest function on average is {min_time_function}")
print(f"The slowest function on average is {max_time_function}")
