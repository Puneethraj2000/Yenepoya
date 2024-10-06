import pygame

# Initialize pygame
pygame.init()

# Set up the screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set up the title of the window
pygame.display.set_caption("Game Over Example")

# Set up the player's lives
lives = 3

# Set up the game over screen
game_over_screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
game_over_screen.fill((255, 0, 0))  # Red background
game_over_font = pygame.font.Font(None, 64)
game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
game_over_screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Simulate the player losing lives
    if lives > 0:
        lives -= 1
        print(f"Lives remaining: {lives}")

    # Check if the player has lost all lives
    if lives <= 0:
        # Display the game over screen
        screen.blit(game_over_screen, (0, 0))
        pygame.display.flip()
        pygame.time.wait(3000)  # Wait for 3 seconds
        pygame.quit()
        sys.exit()

    # Update the screen
    pygame.display.flip()
    pygame.time.Clock().tick(60)