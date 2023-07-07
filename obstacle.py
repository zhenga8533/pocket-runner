import pygame
from util import override


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, type):
        # Obstacle variables
        self.x = x

        # Image control
        super().__init__()
        if type == 0:
            self.image = pygame.image.load(f'assets/obstacles/cacnea.png')
            self.y = 125
        else:
            self.image = pygame.image.load(f'assets/obstacles/cacnea.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]

    @override(pygame.sprite.Sprite)
    def update(self, speed):
        # Player control
        self.x -= speed
        self.rect.topleft = [self.x, self.y]
