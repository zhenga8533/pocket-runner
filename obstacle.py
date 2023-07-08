import pygame
from random import randint
from util import override


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, type):
        # Obstacle variables
        self.x = x

        # Image control
        super().__init__()
        if type == 0:
            self.image = pygame.image.load(f'assets/obstacles/cacnea.png')
            self.y = 155
        elif type == 1:
            self.image = pygame.image.load(f'assets/obstacles/togekiss.png')
            self.y = randint(50, 120)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = [self.x, self.y]

    @override(pygame.sprite.Sprite)
    def update(self, speed):
        # Player control
        self.x -= speed
        self.rect.bottomleft = [self.x, self.y]
