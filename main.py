import pygame
from pygame.locals import *
from player import Player

# Pygame constants
WIDTH = 600
HEIGHT = 200
BACKGROUND = pygame.image.load("assets/background.png")
BACKGROUND = pygame.transform.scale(BACKGROUND, (600, 300))


class Pocket_Runner:
    def __init__(self):
        # Pygame display
        self.w = WIDTH
        self.h = HEIGHT
        self.display = pygame.display.set_mode((self.w, self.h))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Pocket Runner')

        # Player variables
        self.player = Player(50, 115)

        # Game variables
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.player)
        self.background = [0, 600]
        self.speed = 1

    def play_step(self):
        # Background scrolling
        for i in range(len(self.background)):
            self.background[i] -= self.speed

            # Refreshes background
            if self.background[i] < -600:
                del self.background[i]
                self.background.append(600)

        # Player animation
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE or event.key == K_UP:
                    self.player.jump()
        self.player.update()

        # Pygame control
        self.draw()
        self.clock.tick(60)

    def draw(self):
        # Draw background
        for i in range(len(self.background)):
            self.display.blit(BACKGROUND, (self.background[i], -100))

        # Draw player
        self.sprites.draw(self.display)

        pygame.display.flip()


if __name__ == '__main__':
    game = Pocket_Runner()

    # Game loop
    while True:
        game.play_step()
