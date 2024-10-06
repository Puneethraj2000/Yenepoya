# 3. Write a Python program to load an image on a surface and perform 
# transformations in Pygame.

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Image Transformations in Pygame")

# Load an image
image = pygame.image.load('Pygame_logo.gif')  # Replace 'your_image.png' with the path to your image
image_rect = image.get_rect(center=(screen_width // 2, screen_height // 2))

# Transformation functions
def scale_image(image, scale_factor):
    width = int(image.get_width() * scale_factor)
    height = int(image.get_height() * scale_factor)
    return pygame.transform.scale(image, (width, height))

def rotate_image(image, angle):
    return pygame.transform.rotate(image, angle)

def flip_image(image, x_bool, y_bool):
    return pygame.transform.flip(image, x_bool, y_bool)

# Main loop
running = True
scale_factor = 1.0
angle = 0
flip_x, flip_y = False, False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                scale_factor += 0.1
            elif event.key == pygame.K_DOWN:
                scale_factor = max(0.1, scale_factor - 0.1)
            elif event.key == pygame.K_RIGHT:
                angle -= 10
            elif event.key == pygame.K_LEFT:
                angle += 10
            elif event.key == pygame.K_f:
                flip_x = not flip_x
            elif event.key == pygame.K_v:
                flip_y = not flip_y

    # Clear the screen
    screen.fill((255, 255, 255))

    # Apply transformations
    transformed_image = scale_image(image, scale_factor)
    transformed_image = rotate_image(transformed_image, angle)
    transformed_image = flip_image(transformed_image, flip_x, flip_y)
    transformed_image_rect = transformed_image.get_rect(center=(screen_width // 2, screen_height // 2))

    # Draw the transformed image
    screen.blit(transformed_image, transformed_image_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()