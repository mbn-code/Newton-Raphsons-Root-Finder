import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1280, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Newton's Method Visualization")

# Constants
PRECISION = 0.00001  # Desired precision
MAX_ITERATIONS = 100  # Maximum number of iterations
SCALE = 80  # Scale of the graph
GUESS_SPEED = 0.1  # Speed of guessing (adjustable)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Parameters
x = 2  # Initial guess
iterations = 0  # Current number of iterations
animate = False  # Whether to animate the movement of the guess
next_x = None  # Next guess
coefficients = []  # Coefficients of the polynomial function

# Function to generate random coefficients
def generate_coefficients():
    return [random.uniform(-0.01, 0.01) for _ in range(4)]  # Adjust the range to be closer to zero


# Function to evaluate polynomial at x
def f(x):
    return sum(a * x**i for i, a in enumerate(coefficients))

# Function to evaluate derivative at x
def df(x):
    return sum((i + 1) * a * x**i for i, a in enumerate(coefficients[1:]))

# Function to check if root exists within range
def has_root():
    for x_val in range(-200, 201):
        x = x_val / 100
        y = f(x)
        if abs(y) < PRECISION:
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
            x = (event.pos[0] - WIDTH // 2) / SCALE
            iterations = 0
            animate = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                generate_graph()
                x = 2  # Reset guess
                iterations = 0
                animate = False

    # Draw axes, numbers, and function
    pygame.draw.line(screen, BLACK, (0, HEIGHT // 2), (WIDTH, HEIGHT // 2), 2)
    pygame.draw.line(screen, BLACK, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 2)
    for i in range(-WIDTH // (2 * SCALE), WIDTH // (2 * SCALE) + 1):
        pygame.draw.line(screen, BLACK, (i * SCALE + WIDTH // 2, HEIGHT // 2 - 5), (i * SCALE + WIDTH // 2, HEIGHT // 2 + 5), 2)
        text = pygame.font.SysFont(None, 24).render(str(i), True, BLACK)
        screen.blit(text, (i * SCALE + WIDTH // 2 - 5, HEIGHT // 2 + 10))
    for i in range(-HEIGHT // (2 * SCALE), HEIGHT // (2 * SCALE) + 1):
        pygame.draw.line(screen, BLACK, (WIDTH // 2 - 5, -i * SCALE + HEIGHT // 2), (WIDTH // 2 + 5, -i * SCALE + HEIGHT // 2), 2)
        text = pygame.font.SysFont(None, 24).render(str(i), True, BLACK)
        screen.blit(text, (WIDTH // 2 + 10, -i * SCALE + HEIGHT // 2 - 5))
    for x_coord in range(WIDTH):
        x_val = (x_coord - WIDTH // 2) / SCALE
        y_val = f(x_val)
        pygame.draw.circle(screen, BLACK, (x_coord, HEIGHT // 2 - int(y_val * SCALE)), 1)

    # Newton's method
    if animate:
        y = f(x)
        slope = df(x)
        next_x = x - y / slope
        if abs(x - next_x) < 0.01:
            animate = False
        else:
            dx = (next_x - x) * GUESS_SPEED
            x += dx
            iterations += 1

    # Draw tangent
    y = f(x)
    slope = df(x)
    pygame.draw.line(screen, RED, (x * SCALE + WIDTH // 2, HEIGHT // 2 - int(y * SCALE)), ((x - y / slope) * SCALE + WIDTH // 2, HEIGHT // 2), 2)
    pygame.draw.circle(screen, BLUE, (x * SCALE + WIDTH // 2, HEIGHT // 2 - int(y * SCALE)), 5)

    # Draw line from tangent to x-axis
    pygame.draw.line(screen, RED, ((x - y / slope) * SCALE + WIDTH // 2, HEIGHT // 2), ((x - y / slope) * SCALE + WIDTH // 2, HEIGHT // 2 - int(y * SCALE)), 2)

    # Draw x value
    text = pygame.font.SysFont(None, 24).render(f"x: {x:.3f}", True, BLACK)
    screen.blit(text, ((x - y / slope) * SCALE + WIDTH // 2, HEIGHT // 2 + 10))

    # Draw y value
    text = pygame.font.SysFont(None, 24).render(f"y: {y:.3f}", True, BLACK)
    screen.blit(text, (10, HEIGHT // 2 - y * SCALE))

    # Draw function formula
    text = pygame.font.SysFont(None, 24).render(f"f(x) = {' + '.join([f'{a:.2f}x^{i}' for i, a in enumerate(coefficients)])}", True, BLACK)
    screen.blit(text, (10, 50))

    # Draw derivative formula
    text = pygame.font.SysFont(None, 24).render(f"f'(x) = {' + '.join([f'{(i+1)*a:.2f}x^{i}' for i, a in enumerate(coefficients[1:])])}", True, BLACK)
    screen.blit(text, (10, 80))

    # Draw current guess
    text = pygame.font.SysFont(None, 24).render(f"Current Guess: {x:.3f}", True, BLACK)
    screen.blit(text, (10, 110))

    # Draw value of function at current guess
    text = pygame.font.SysFont(None, 24).render(f"f(Current Guess): {y:.3f}", True, BLACK)
    screen.blit(text, (10, 140))

    # Draw value of derivative at current guess
    text = pygame.font.SysFont(None, 24).render(f"f'(Current Guess): {slope:.3f}", True, BLACK)
    screen.blit(text, (10, 170))

    # Draw iterations
    text = pygame.font.SysFont(None, 24).render(f"Iterations: {iterations}", True, BLACK)
    screen.blit(text, (10, 200))

    # Draw "New Graph" button
    pygame.draw.rect(screen, GREEN, (WIDTH - 150, 20, 120, 40))
    text = pygame.font.SysFont(None, 24).render("New Graph", True, BLACK)
    screen.blit(text, (WIDTH - 140, 30))

    pygame.display.flip()

pygame.quit()
