# 1. Write a Python program to initialize Pygame and create a window.

import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((600,340))
pygame.display.set_caption("1st")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    

# Quit Pygame
pygame.quit()