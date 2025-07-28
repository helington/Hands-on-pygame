import pygame
from os import path
from random import choice

from src.player import Player
from src.obstacle import Obstacle
from src.constants import (
    GRAPHICS_DIR,
    GRAPHICS_PLAYER_DIR,
    FONT_DIR,
    HEIGHT_SCREEN,
    WIDTH_SCREEN,
    FPS,
    FONT_SIZE,
    DARKISH_GRAY,
    DARKISH_CYAN,
    LIGHT_CYAN
)

class Game:
    def __init__(self):

        # Set up pygame
        pygame.init()
        pygame.display.set_caption('Runner')
        pygame.joystick.init()
        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
        else:
            self.joystick = None
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))

        # Set up data
        font_path = path.join(FONT_DIR, 'Pixeltype.ttf')
        sky_path = path.join(GRAPHICS_DIR, 'Sky.png')
        ground_path = path.join(GRAPHICS_DIR, 'ground.png')
        self.font = pygame.font.Font(font_path, FONT_SIZE)
        self.sky = pygame.image.load(sky_path).convert()
        self.ground = pygame.image.load(ground_path).convert()

        # Set up intro screen
        player_stantard_path = path.join(GRAPHICS_PLAYER_DIR, 'player_stand.png')
        self.player_standard = pygame.image.load(player_stantard_path).convert_alpha()
        self.player_standard = pygame.transform.rotozoom(self.player_standard, 0, 2)
        self.player_standard_rectangle = self.player_standard.get_rect(center = (400, 200))

        button = 'enter' if self.joystick is None else 'start'
        self.game_message = self.font.render(f'Press {button} to run', False, LIGHT_CYAN)
        self.game_message_rectangle = self.game_message.get_rect(center = (400, 340))

        self.game_name = self.font.render('Pixel Runner', False, LIGHT_CYAN)
        self.game_name_rectangle = self.game_name.get_rect(center = (400, 80))

        # Set up Timer
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer,1500)

        # Set up atributes
        self.game_active = False
        self.start_time = 0
        self.score = 0

        # Set up groups
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player(self.joystick))
        self.obstacle_group = pygame.sprite.Group()

    def display_score(self, start_time, font):
        self.score = int(pygame.time.get_ticks() / 1000) - start_time
        score_surface = font.render(f'Score: {self.score}', False, DARKISH_GRAY)
        score_rectangle = score_surface.get_rect(center=(400, 50))
        self.screen.blit(score_surface, score_rectangle)

    def collision_sprite(self):
        if pygame.sprite.spritecollide(self.player.sprite, self.obstacle_group, False):
            self.obstacle_group.empty()
            self.game_active = False
        else: self.game_active = True

    def run(self):

        # Game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if self.game_active:
                    if event.type == self.obstacle_timer:
                        self.obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))
                else:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        self.game_active = True
                        self.start_time = int(pygame.time.get_ticks() / 1000)

                    elif event.type == pygame.JOYBUTTONDOWN:
                        if event.button == 6:
                            self.game_active = True
                            self.start_time = int(pygame.time.get_ticks() / 1000)

            if self.game_active:
                self.screen.blit(self.sky, (0, 0))
                self.screen.blit(self.ground, (0, self.sky.get_height()))

                self.display_score(self.start_time, self.font)

                self.player.draw(self.screen)
                self.player.update()

                self.obstacle_group.draw(self.screen)
                self.obstacle_group.update()

                self.collision_sprite()

            else:
                self.screen.fill(DARKISH_CYAN)
                self.screen.blit(self.game_name, self.game_name_rectangle)

                score_message = self.font.render(f'Your score: {self.score}', False, LIGHT_CYAN)
                score_message_rectangle = score_message.get_rect(center = (400, 330))

                self.screen.blit(self.player_standard, self.player_standard_rectangle)

                if self.score != 0:
                    self.screen.blit(score_message, score_message_rectangle)
                    self.game_message_rectangle = self.game_message.get_rect(center = (400, 370))
                self.screen.blit(self.game_message, self.game_message_rectangle)

            # Update display
            pygame.display.update()

            # Cap the frame rate
            self.clock.tick(FPS)

        pygame.quit()
