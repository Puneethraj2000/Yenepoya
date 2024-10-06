"""1. Write a Python program to use text as buttons with event handling and display image in the same 
window after clicking the button in Pygame."""

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set window size and title
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Text Button Event Handling")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Load image
image = pygame.image.load('Pygame_logo.gif')
image_rect = image.get_rect(center=(screen_width // 2, screen_height // 2))

# Define font
font = pygame.font.SysFont(None, 40)

# Button class
class Button:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = GRAY

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surf = font.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

# Create buttons
button1 = Button('Show Image', 100, 50, 200, 50)

# Main loop
running = True
show_image = False
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button1.rect.collidepoint(event.pos):
                show_image = True
                print("Button clicked: Show Image")  # Print statement for event handling

    # Draw buttons
    button1.draw(screen)

    # Display image if button is clicked
    if show_image:
        screen.blit(image, image_rect)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()