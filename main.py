import pygame

# Pygame constants
WIDTH = 600
HEIGHT = 300
BACKGROUND = pygame.image.load("background.png")


class Pocket_Runner:
    def __init__(self):
        # Pygame display
        self.w = WIDTH
        self.h = HEIGHT
        self.display = pygame.display.set_mode((self.w, self.h))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Pocket Runner')

        # Player variables
        self.y = 0

        # Game variables
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

        # Pygame control
        self.draw()
        self.clock.tick(60)

    def draw(self):
        # Draw background
        for i in range(len(self.background)):
            self.display.blit(BACKGROUND, (self.background[i], -15))

        pygame.display.flip()


if __name__ == '__main__':
    game = Pocket_Runner()

    # Game loop
    while True:
        game.play_step()
