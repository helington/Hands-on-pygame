import pygame
from os import path
from random import randint

from src.constants import (
    GRAPHICS_SNAIL_DIR, GRAPHICS_FLY_DIR
)

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'fly':
            fly_1_path = path.join(GRAPHICS_FLY_DIR, 'Fly1.png')
            fly_2_path = path.join(GRAPHICS_FLY_DIR, 'Fly2.png')
            fly_1 = pygame.image.load(fly_1_path).convert_alpha()
            fly_2 = pygame.image.load(fly_2_path).convert_alpha()
            
            self.frames = [fly_1, fly_2]
            y_pos = 210
        else:
            snail_1_path = path.join(GRAPHICS_SNAIL_DIR, 'snail1.png')
            snail_2_path = path.join(GRAPHICS_SNAIL_DIR, 'snail2.png')
            snail_1 = pygame.image.load(snail_1_path).convert_alpha()
            snail_2 = pygame.image.load(snail_2_path).convert_alpha()
            
            self.frames = [snail_1, snail_2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()