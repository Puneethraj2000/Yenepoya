# 4. Write a Python program to handle keyboard and mouse events in Pygame.

# Import the Pygame library
import pygame

# Initialize Pygame
pygame.init()

# Set up display
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Event Handling in Pygame")

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print(f"Key {pygame.key.name(event.key)} pressed")
        elif event.type == pygame.KEYUP:
            print(f"Key {pygame.key.name(event.key)} released")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                print(f"Left mouse button clicked at {event.pos}")
            elif event.button == 2:  # Middle mouse button
                print(f"Middle mouse button clicked at {event.pos}")
            elif event.button == 3:  # Right mouse button
                print(f"Right mouse button clicked at {event.pos}")
        elif event.type == pygame.MOUSEBUTTONUP:
            print(f"Mouse button released at {event.pos}")
        elif event.type == pygame.MOUSEMOTION:
            print(f"Mouse moved to {event.pos}")

    # Fill the screen with a color
    screen.fill((0, 0, 0))
    pygame.display.flip()

# Quit Pygame
pygame.quit()