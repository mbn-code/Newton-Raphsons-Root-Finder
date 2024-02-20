import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Newton's Method Visualization")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Parameters
x = 2  # Initial guess
precision = 0.00001  # Desired precision
max_iterations = 100  # Maximum number of iterations
iterations = 0  # Current number of iterations
animate = False  # Whether to animate the movement of the guess
next_x = None  # Next guess
coefficients = []  # Coefficients of the polynomial function
scale = 80  # Scale of the graph
guess_speed = 0.1  # Speed of guessing (adjustable)

# Function to generate random coefficients
def generate_coefficients():
    return [random.uniform(-1, 1) for _ in range(3)]

# Function to evaluate polynomial at x
def f(x):
    return sum(a * x**i for i, a in enumerate(coefficients))

# Function to evaluate derivative at x
def df(x):
    return sum((i + 1) * a * x**i for i, a in enumerate(coefficients[1:]))

# Function to check if root exists within range
def has_root():
    """
    Checks if the function f(x) has a root within the given range.

    Returns:
        bool: True if a root is found, False otherwise.
    """
    for x_val in range(-200, 201):
        x = x_val / 100
        y = f(x)
        if abs(y) < precision:
            return True
    return False

# Function to generate graph
def generate_graph():
    global coefficients
    coefficients = generate_coefficients()
    if not has_root():
        generate_graph()

# Initialize coefficients and graph
generate_graph()

# Main loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not animate:
            x = (event.pos[0] - WIDTH // 2) / scale
            iterations = 0
            animate = True

    # Draw axes
    pygame.draw.line(screen, BLACK, (0, HEIGHT // 2), (WIDTH, HEIGHT // 2), 2)
    pygame.draw.line(screen, BLACK, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 2)

    # Draw numbers on axes
    for i in range(-WIDTH // (2 * scale), WIDTH // (2 * scale) + 1):
        pygame.draw.line(screen, BLACK, (i * scale + WIDTH // 2, HEIGHT // 2 - 5), (i * scale + WIDTH // 2, HEIGHT // 2 + 5), 2)
        text = pygame.font.SysFont(None, 24).render(str(i), True, BLACK)
        screen.blit(text, (i * scale + WIDTH // 2 - 5, HEIGHT // 2 + 10))
    for i in range(-HEIGHT // (2 * scale), HEIGHT // (2 * scale) + 1):
        pygame.draw.line(screen, BLACK, (WIDTH // 2 - 5, -i * scale + HEIGHT // 2), (WIDTH // 2 + 5, -i * scale + HEIGHT // 2), 2)
        text = pygame.font.SysFont(None, 24).render(str(i), True, BLACK)
        screen.blit(text, (WIDTH // 2 + 10, -i * scale + HEIGHT // 2 - 5))

    # Draw function
    for x_coord in range(WIDTH):
        x_val = (x_coord - WIDTH // 2) / scale
        y_val = f(x_val)
        pygame.draw.circle(screen, BLACK, (x_coord, HEIGHT // 2 - int(y_val * scale)), 1)

    # Newton's method
    if animate:
        y = f(x)
        slope = df(x)
        next_x = x - y / slope
        if abs(x - next_x) < 0.01:
            animate = False
        else:
            dx = (next_x - x) * guess_speed  # Calculate the incremental change
            x += dx  # Update the guess position
            iterations += 1

    # Draw tangent
    y = f(x)
    slope = df(x)
    pygame.draw.line(screen, RED, (x * scale + WIDTH // 2, HEIGHT // 2 - int(y * scale)), ((x - y / slope) * scale + WIDTH // 2, HEIGHT // 2), 2)
    pygame.draw.circle(screen, BLUE, (x * scale + WIDTH // 2, HEIGHT // 2 - int(y * scale)), 5)

    # Draw line from tangent to x-axis
    pygame.draw.line(screen, RED, ((x - y / slope) * scale + WIDTH // 2, HEIGHT // 2), ((x - y / slope) * scale + WIDTH // 2, HEIGHT // 2 - int(y * scale)), 2)

    # Draw x value
    text = pygame.font.SysFont(None, 24).render(f"x: {x:.3f}", True, BLACK)
    screen.blit(text, ((x - y / slope) * scale + WIDTH // 2, HEIGHT // 2 + 10))

    # Draw y value
    text = pygame.font.SysFont(None, 24).render(f"y: {y:.3f}", True, BLACK)
    screen.blit(text, (10, HEIGHT // 2 - y * scale))

    # Draw iterations
    text = pygame.font.SysFont(None, 24).render(f"Iterations: {iterations}", True, BLACK)
    screen.blit(text, (10, 30))

    pygame.display.flip()

pygame.quit()
