import pygame
from pygame.version import PygameVersion
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    # new instance of GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # set FPS to 60
    clock: pygame.time.Clock = pygame.time.Clock()
    dt: float = 0.0

    # creates game loop
    while True:
        log_state()
        # Pygame event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # draw screen
        screen.fill("black")
        pygame.display.flip()

        # limit FPS to 60 and get delta time
        dt = clock.tick(60) / 1000































if __name__ == "__main__":
    main()
