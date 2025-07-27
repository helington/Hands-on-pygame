import pygame
from os import path

from constants import (
    GRAPHICS_DIR,
    AUDIO_DIR,
    FONT_DIR,
    HEIGHT_SCREEN,
    WIDTH_SCREEN,
    FPS
)

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
pygame.display.set_caption('Runner')

# Clock to control the ceil frame rate
clock = pygame.time.Clock()

# Create a surface for sky image
sky_path = path.join(GRAPHICS_DIR, 'Sky.png')
sky_surface = pygame.image.load(sky_path)

# Crate a surface for ground image
ground_path = path.join(GRAPHICS_DIR, 'ground.png')
ground_path = pygame.image.load(ground_path)

# Game loop
running = True
while running:

    # Loop through all available events
    for event in pygame.event.get():

        # pygame.QUIT event means the user clicked X to close your window
        if event.type == pygame.QUIT:
            running = False

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_path, (0, sky_surface.get_height()))

    # Update display
    pygame.display.update()

    # Cap the frame rate
    clock.tick()

pygame.quit(FPS)