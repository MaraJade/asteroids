import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    pl = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pl.update(dt)

        screen.fill(color="black")
        pl.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
