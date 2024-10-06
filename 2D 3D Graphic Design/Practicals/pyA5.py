# 5. Write a Python program to draw basic shapes (lines, rectangles, circles) 
# in Pygame.

# Import the Pygame library
import pygame

# Initialize Pygame
pygame.init()

# Set up display
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Drawing Shapes in Pygame")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw a red line
    pygame.draw.line(screen, RED, (100, 100), (700, 100), 5)

    # Draw a green rectangle
    pygame.draw.rect(screen, GREEN, (150, 200, 500, 100))

    # Draw a blue circle
    pygame.draw.circle(screen, BLUE, (400, 400), 75)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()