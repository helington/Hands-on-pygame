from os import path

import pygame

from src.constants import AUDIO_DIR, FLOOR_Y, GRAPHICS_PLAYER_DIR


class Player(pygame.sprite.Sprite):
    def __init__(self, joystick):
        super().__init__()

        player_walk_1_path = path.join(
            GRAPHICS_PLAYER_DIR, 'player_walk_1.png'
        )
        player_walk_2_path = path.join(
            GRAPHICS_PLAYER_DIR, 'player_walk_2.png'
        )
        player_jump_path = path.join(GRAPHICS_PLAYER_DIR, 'jump.png')
        player_walk_1 = pygame.image.load(player_walk_1_path).convert_alpha()
        player_walk_2 = pygame.image.load(player_walk_2_path).convert_alpha()

        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load(player_jump_path).convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0
        self.joystick = joystick
        self.is_jumping = False

        jump_soung_path = path.join(AUDIO_DIR, 'jump.mp3')
        self.jump_sound = pygame.mixer.Sound(jump_soung_path)
        self.jump_sound.set_volume(0.5)

    def player_input(self):
        if self.rect.bottom >= FLOOR_Y and not self.is_jumping:
            keys = pygame.key.get_pressed()
            space_pressed = keys[pygame.K_SPACE]

            if self.joystick:
                jump_button_pressed = self.joystick.get_button(0)
            else:
                jump_button_pressed = False

            jump_input = space_pressed or jump_button_pressed

            if jump_input:
                self.gravity = -20
                self.is_jumping = True
                self.jump_sound.play()

    def animation_state(self):
        if self.rect.bottom < FLOOR_Y:
            self.image = self.player_jump
        else:
            self.is_jumping = False
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        self.rect.bottom = min(FLOOR_Y, self.rect.bottom)

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()
