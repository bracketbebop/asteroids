
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()

    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Assign Player class to both groups
    Player.containers = (updatable, drawable)

    # Instantiate player object
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    # New instance of GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set FPS to 60
    clock: pygame.time.Clock = pygame.time.Clock()
    dt: float = 0.0

    # Create game loop
    while True:
        # Pygame event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Update all objects in the updatable group
        updatable.update(dt)
        log_state()

        # Draw screen
        screen.fill("black")

        # Draw every object in the drawable group
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # Limit FPS to 60 and get delta time
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
