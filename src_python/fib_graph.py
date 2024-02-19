import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to generate Fibonacci sequence
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Function to calculate the golden ratio
def golden_ratio(n):
    fib_sequence = fibonacci(n)
    ratios = [fib_sequence[i+1] / fib_sequence[i] for i in range(1, len(fib_sequence)-1)]
    return ratios

# Create Fibonacci sequence and corresponding golden ratios
n_terms = 16  # Increase this to generate more terms
fib_sequence = fibonacci(n_terms)
ratios = golden_ratio(n_terms)

# Create figure and axis
fig, ax1 = plt.subplots()

# Initialize plot for Fibonacci sequence
ax1.set_xlim(0, n_terms)
ax1.set_ylim(0, max(fib_sequence) * 1.1)
ax1.set_title('Fibonacci Sequence and Golden Ratio')
line1, = ax1.plot([], [], lw=2, color='blue', label='Fibonacci Sequence')

# Create a second axis for the golden ratio
ax2 = ax1.twinx()
ax2.set_ylim(0, max(ratios) * 1.1)
line2, = ax2.plot([], [], lw=2, color='red', label='Golden Ratio')

# Initialize text
text = ax1.text(0.02, 0.95, '', transform=ax1.transAxes)

# Function to update the plot
def update(num, fib_sequence, ratios, line1, line2):
    line1.set_data(range(num), fib_sequence[:num])
    line2.set_data(range(num), ratios[:num])
    return line1, line2

# Create animation
ani = animation.FuncAnimation(fig, update, frames=n_terms, fargs=[fib_sequence, ratios, line1, line2])

plt.show()