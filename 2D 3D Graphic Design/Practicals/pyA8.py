# 8. Write a Python program to move an image using numeric keypads and 
# the mouse in Pygame.

import pygame

# Initialize Pygame
pygame.init()

# Set up display
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Move Image with Keypad and Mouse")

# Load image
image = pygame.image.load('Pygame_logo.gif')
image_rect = image.get_rect()
image_rect.topleft = (100, 100)  # Initial position

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                image_rect.center = event.pos

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Move image with numeric keypad
    if keys[pygame.K_KP4]:  # Keypad 4 - Move left
        image_rect.x -= 5
    if keys[pygame.K_KP6]:  # Keypad 6 - Move right
        image_rect.x += 5
    if keys[pygame.K_KP8]:  # Keypad 8 - Move up
        image_rect.y -= 5
    if keys[pygame.K_KP2]:  # Keypad 2 - Move down
        image_rect.y += 5

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Draw the image
    screen.blit(image, image_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()