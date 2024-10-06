# 7. Write a Python program to load and customize the cursor in Pygame.

import pygame
import os

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Custom Cursor Example')

# Load custom cursor image
cursor_image = pygame.image.load('Pygame_logo.gif')
cursor_image = pygame.transform.scale(cursor_image, (32, 32))  # Scale cursor image to desired size
cursor_rect = cursor_image.get_rect()

# Hide the default cursor
pygame.mouse.set_visible(False)

# Main loop
running = True
while running:
    screen.fill((255, 255, 255))  # Fill the screen with white

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get mouse position and update cursor rect position
    cursor_rect.center = pygame.mouse.get_pos()

    # Draw custom cursor
    screen.blit(cursor_image, cursor_rect.topleft)

    # Update the display
    pygame.display.flip()

pygame.quit()