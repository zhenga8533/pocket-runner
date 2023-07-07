import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

        # Image control
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

    def update(self):
        self.rect.topleft = [self.x, self.y]
        self.frame = (self.frame + 0.2) % 4
        self.image = self.sprites[int(self.frame)]
