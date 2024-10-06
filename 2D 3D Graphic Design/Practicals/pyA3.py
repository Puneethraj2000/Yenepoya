# 3. Write a Python program to set and change the window size and title in 
# Pygame.

# Import the Pygame library
import pygame

# Initialize Pygame
pygame.init()

# Set the initial window size
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

# Set the initial window title
pygame.display.set_caption("Initial Title")

# Function to change the window size
def change_window_size(new_size):
    global screen
    screen = pygame.display.set_mode(new_size)
    pygame.display.flip()

# Function to change the window title
def change_window_title(new_title):
    pygame.display.set_caption(new_title)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                change_window_size((640, 480))
            elif event.key == pygame.K_2:
                change_window_size((1024, 768))
            elif event.key == pygame.K_t:
                change_window_title("New Title")
            elif event.key == pygame.K_p:
                change_window_title("Title")

    # Fill the screen with a color
    screen.fill((0,0,0))
    pygame.display.flip()

# Quit Pygame
pygame.quit()