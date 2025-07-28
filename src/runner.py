import pygame
from os import path
from random import randint

from constants import (
    GRAPHICS_DIR,
    GRAPHICS_SNAIL_DIR,
    GRAPHICS_PLAYER_DIR,
    GRAPHICS_FLY_DIR,
    AUDIO_DIR,
    FONT_DIR,
    HEIGHT_SCREEN,
    WIDTH_SCREEN,
    FPS,
    FONT_SIZE,
    DARKISH_GRAY,
    DARKISH_CYAN,
    LIGHT_CYAN
)

def display_score(start_time, font):
    current_score = int(pygame.time.get_ticks() / 1000) - start_time

    # Create a surface for score
    score_surface = font.render(f'Score: {current_score}', False, DARKISH_GRAY)

    score_rectangle = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rectangle)

    return current_score

def obstacle_movement(obstacle_rect_list, snail_surface, fly_surface):
    if obstacle_rect_list:
        for obstacle_rect in obstacle_rect_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)

        obstacle_rect_list = [
            obstacle for obstacle in obstacle_rect_list if obstacle.left > -100
        ]

        return obstacle_rect_list
    else: return list()

def collisions(player, obstacles):
    if obstacles:
        for obstacles_rect in obstacles:
            if player.colliderect(obstacles_rect): return False
    
    return True

def player_animation(player_surface, player_index, player_rectangle, player_walk, player_jump):
    if player_rectangle.bottom < 300:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surface = player_walk[int(player_index)]

    return player_surface, player_index

pygame.joystick.init()
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print("Using joystick:", joystick.get_name())
else:
    joystick = None
    print("No joystick found.")


# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
pygame.display.set_caption('Runner')
font_path = path.join(FONT_DIR, 'Pixeltype.ttf')
font = pygame.font.Font(font_path, FONT_SIZE)
game_active = False
start_time = 0
is_jumping = False

# Clock to control the ceil frame rate
clock = pygame.time.Clock()

# Create a surface for sky image
sky_path = path.join(GRAPHICS_DIR, 'Sky.png')
sky_surface = pygame.image.load(sky_path).convert()

# Crate a surface for ground image
ground_path = path.join(GRAPHICS_DIR, 'ground.png')
ground_path = pygame.image.load(ground_path).convert()

# Snail
snail_frame_1_path = path.join(GRAPHICS_SNAIL_DIR, 'snail1.png')
snail_frame_1 = pygame.image.load(snail_frame_1_path).convert_alpha()
snail_frame_2_path = path.join(GRAPHICS_SNAIL_DIR, 'snail2.png')
snail_frame_2 = pygame.image.load(snail_frame_2_path).convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surface = snail_frames[snail_frame_index]

# Fly
fly_frame_1_path = path.join(GRAPHICS_FLY_DIR, 'Fly1.png')
fly_frame_1 = pygame.image.load(fly_frame_1_path).convert_alpha()
fly_frame_2_path = path.join(GRAPHICS_FLY_DIR, 'Fly2.png')
fly_frame_2 = pygame.image.load(fly_frame_2_path).convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]

obstacle_rect_list = list()

# Player
player_walk_1_path = path.join(GRAPHICS_PLAYER_DIR, 'player_walk_1.png')
player_walk_1 = pygame.image.load(player_walk_1_path)
player_walk_2_path = path.join(GRAPHICS_PLAYER_DIR, 'player_walk_2.png')
player_walk_2 = pygame.image.load(player_walk_2_path)
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump_path = path.join(GRAPHICS_PLAYER_DIR, 'jump.png')
player_jump = pygame.image.load(player_jump_path)

player_surface = player_walk[player_index]
player_rectangle = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0

# Intro screen
player_stantard_path = path.join(GRAPHICS_PLAYER_DIR, 'player_stand.png')
player_standard = pygame.image.load(player_stantard_path).convert_alpha()
player_standard = pygame.transform.rotozoom(player_standard, 0, 2)
player_standard_rectangle = player_standard.get_rect(center = (400, 200))

score = 0
game_name = font.render('Pixel Runner', False, LIGHT_CYAN)
game_name_rectangle = game_name.get_rect(center = (400, 80))

button = 'enter' if joystick is None else 'start'

game_message = font.render(f'Press {button} to run', False, LIGHT_CYAN)
game_message_rectangle = game_message.get_rect(center = (400, 340))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)


# Game loop
running = True
while running:

    # Loop through all available events
    for event in pygame.event.get():

        # pygame.QUIT event means the user clicked X to close your window
        if event.type == pygame.QUIT:
            running = False

        if game_active:

            if event.type == obstacle_timer:
                if randint(0, 2):
                    surface_to_add = fly_surface.get_rect(bottomright=(randint(900, 1100), 300))
                else:
                    surface_to_add = fly_surface.get_rect(bottomright=(randint(900, 1100), 210))
                obstacle_rect_list.append(surface_to_add)
            elif event.type == snail_animation_timer:
                if snail_frame_index == 0: snail_frame_index = 1
                else: snail_frame_index = 0
                snail_surface = snail_frames[snail_frame_index]
            elif event.type == fly_animation_timer:
                if fly_frame_index == 0: fly_frame_index = 1
                else: fly_frame_index = 0
                fly_surface = fly_frames[fly_frame_index]
            
        else:

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == 6:
                    game_active = True
                    start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:

        # Jumping
        if player_rectangle.bottom >= 300 and not is_jumping:
            keys = pygame.key.get_pressed()
            space_pressed = keys[pygame.K_SPACE]

            if joystick:
                jump_button_pressed = joystick.get_button(0)
            else:
                jump_button_pressed = False

            jump_input = space_pressed or jump_button_pressed

            if jump_input:
                player_gravity = -20
                is_jumping = True
        
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_path, (0, sky_surface.get_height()))
        score = display_score(start_time=start_time, font=font)

        # Player
        player_gravity += 1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= 300:
            is_jumping = False
            player_rectangle.bottom = 300
        player_surface, player_index = player_animation(
            player_surface, player_index, player_rectangle, player_walk, player_jump
        )
        screen.blit(player_surface, player_rectangle)

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list, snail_surface, fly_surface)

        # Collision
        game_active = collisions(player_rectangle, obstacle_rect_list)
    else:
        screen.fill(DARKISH_CYAN)
        screen.blit(game_name, game_name_rectangle)

        is_jumping = False
        obstacle_rect_list.clear()
        player_rectangle.midbottom == (80, 300)
        player_gravity = 0

        score_message = font.render(f'Your score: {score}', False, LIGHT_CYAN)
        score_message_rectangle = score_message.get_rect(center = (400, 330))

        screen.blit(player_standard, player_standard_rectangle)

        if score != 0:
            screen.blit(score_message, score_message_rectangle)
            game_message_rectangle = game_message.get_rect(center = (400, 370))

        screen.blit(game_message, game_message_rectangle)

    # Update display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(FPS)

pygame.quit()