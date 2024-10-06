# 6. Write a Python program to develop flappy game in Pygame.

import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Bird settings
BIRD_WIDTH, BIRD_HEIGHT = 40, 40
bird = pygame.Rect(WIDTH // 4, HEIGHT // 2, BIRD_WIDTH, BIRD_HEIGHT)
bird_speed = 0
gravity = 0.5
jump = -10

# Pipe settings
PIPE_WIDTH = 70
PIPE_HEIGHT = 400
pipe_gap = 150
pipe_speed = 3
pipe_frequency = 1500  # milliseconds
last_pipe = pygame.time.get_ticks() - pipe_frequency

pipes = []

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speed = jump

    # Bird movement
    bird_speed += gravity
    bird.y += bird_speed

    # Generate pipes
    time_now = pygame.time.get_ticks()
    if time_now - last_pipe > pipe_frequency:
        pipe_top = pygame.Rect(WIDTH, 0, PIPE_WIDTH, random.randint(100, HEIGHT - pipe_gap - 100))
        pipe_bottom = pygame.Rect(WIDTH, pipe_top.height + pipe_gap, PIPE_WIDTH, HEIGHT - pipe_top.height - pipe_gap)
        pipes.append(pipe_top)
        pipes.append(pipe_bottom)
        last_pipe = time_now

    # Move pipes
    for pipe in pipes:
        pipe.x -= pipe_speed

    # Remove off-screen pipes
    pipes = [pipe for pipe in pipes if pipe.x + PIPE_WIDTH > 0]

    # Check for collisions
    for pipe in pipes:
        if bird.colliderect(pipe):
            running = False

    if bird.top <= 0 or bird.bottom >= HEIGHT:
        running = False

    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, bird)
    for pipe in pipes:
        pygame.draw.rect(screen, BLACK, pipe)

    # Update display
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()