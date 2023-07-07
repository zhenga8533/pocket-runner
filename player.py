import pygame
from util import override

GRAVITY = -0.9


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Player variables
        self.x = x
        self.y = y
        self.ground = y
        self.acceleration = 0

        # Image control
        super().__init__()
        self.sprites = []
        for i in range(1, 5):
            sprite = pygame.image.load(f'assets/player/player_{i}.png')
            sprite = pygame.transform.scale(sprite, (40, 40))
            sprite = pygame.transform.flip(sprite, True, False)
            self.sprites.append(sprite)
        self.frame = 0
        self.image = self.sprites[self.frame]
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]

    @override(pygame.sprite.Sprite)
    def update(self):
        # Player control
        self.acceleration += GRAVITY
        if self.y <= self.ground:
            self.y = min(self.ground, self.y - self.acceleration)

        # Update image
        self.rect.topleft = [self.x, self.y]
        self.frame = (self.frame + 0.2) % 4
        self.image = self.sprites[int(self.frame)]
        if self.y < self.ground:
            self.image = pygame.transform.rotate(self.image, 30)

    def jump(self):
        self.acceleration = 13 * -GRAVITY
