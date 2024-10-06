# 6. Write a Python program to load and display an image using Pygame.

# Import the Pygame library
import pygame

# Initialize Pygame
pygame.init()

# Set up display
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Display Image in Pygame")

# Load an image
image_path = 'Pygame_logo.gif'  # Replace with the path to your image file
image = pygame.image.load(image_path)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Display the image
    screen.blit(image, (100, 100))  # Draw the image at (100, 100)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()