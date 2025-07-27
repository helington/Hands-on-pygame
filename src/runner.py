import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')

# Clock to control the ceil frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:

    # Loop through all available events
    for event in pygame.event.get():

        # pygame.QUIT event means the user clicked X to close your window
        if event.type == pygame.QUIT:
            running = False

    # Update display
    pygame.display.update()

    # Cap the frame rate
    clock.tick()

pygame.quit()