#Using Pygame

import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Line y = mx + b")

# Define line parameters
m = 0.5  # Slope
b = 100  # Y-intercept (in pixels)

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Draw loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(black)

    # Draw the line
    for x in range(0, width):
        y = int(m * x + b)
        if 0 <= y < height:
            pygame.draw.circle(screen, white, (x, height - y), 1)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
