import pygame
from pygame import key
from pygame.locals import *
import random
from player import Player
from obstacle import Obstacle

# Pygame constants
pygame.init()
WIDTH = 600
HEIGHT = 200
FONT = pygame.font.Font("assets/pokemon_font.ttf", 18)
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
        self.player = Player(50, 155)

        # Game variables
        self.start = False
        self.speed = 3
        self.score = 0
        self.obstacles = [Obstacle(800, 0)]
        self.next_obstacle = 100

        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.player)
        self.sprites.add(self.obstacles)
        self.background = [0, 600]
        self.draw()

    def play_step(self):
        # Game control
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                self.start = True
            elif event.type == KEYUP and event.key == K_DOWN:
                self.player.stretch()
        if not self.start:
            return

        # Player control
        keys = key.get_pressed()
        if keys[K_q]:
            pygame.quit()
            quit()
        if keys[K_SPACE]:
            self.player.jump()
            self.start = True
        if keys[K_DOWN]:
            self.player.down()
            if self.player.y == self.player.ground and self.player.rect.height == 40:
                self.player.crouch()

        # Background scrolling
        for i in range(len(self.background)):
            self.background[i] -= self.speed

            # Refreshes background
            if self.background[i] < -600:
                del self.background[i]
                self.background.append(600)

        # Obstacle control
        for i in range (len(self.obstacles)):
            self.obstacles[i].update(self.speed)

            # Check for collision
            if self.player.rect.colliderect(self.obstacles[i].rect):
                pygame.quit()
                quit()

            # Delete sprite when off screen
            if self.obstacles[i].x < -self.obstacles[i].image.get_width():
                self.obstacles[i].kill()

        # Generate obstacles
        if self.score == self.next_obstacle:
            obstacle = Obstacle(800, random.randint(0, 1))
            self.obstacles.append(obstacle)
            self.sprites.add(obstacle)
            self.next_obstacle += int(random.randint(50, 200) / (1 + self.score/1000))

        # Player animation
        self.player.update(self.speed / (3.14**3))

        # Pygame control
        self.score += 1
        if self.score % 100 == 0:
            self.speed += 0.1
        self.draw()
        self.clock.tick(60)

    def draw(self):
        # Draw background
        for i in range(len(self.background)):
            self.display.blit(BACKGROUND, (self.background[i], -100))

        # Draw sprites
        self.sprites.draw(self.display)

        # Position and draw score
        score = FONT.render(f'HI: 1000  SCORE: {int(self.score)}', True, (0, 0, 0))
        score_rect = score.get_rect()
        score_rect.right = self.w - 10
        score_rect.bottom = score_rect.h + 10
        self.display.blit(score, score_rect)

        pygame.display.flip()


if __name__ == '__main__':
    game = Pocket_Runner()

    # Game loop
    while True:
        game.play_step()
