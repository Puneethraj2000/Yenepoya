# 2. Write a Python program to change the screen background color in Pygame.

# Importing the library
import pygame
import sys
import random

# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Change Background Color')

# Function to generate a random color
def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Function to draw the button
def draw_button(surface, rect, color, text):
    pygame.draw.rect(surface, color, rect)
    font = pygame.font.SysFont(None, 24)
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)

# Initializing RGB Color
color = get_random_color()
button_color = (200, 200, 200)
button_rect = pygame.Rect(150, 130, 120, 40)

# Main loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                color = get_random_color()
    
    # Changing surface color
    surface.fill(color)
    draw_button(surface, button_rect, button_color, 'Change Color')
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()