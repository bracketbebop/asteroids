import random
import pygame
from pygame.math import Vector2
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event



class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface) -> None:
        circle = pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)


    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")

            angle: float = random.uniform(20, 50)
            velosity_one: Vector2 = pygame.math.Vector2.rotate(self.velocity, angle)
            velosity_two: Vector2 = pygame.math.Vector2.rotate(self.velocity, -angle)
            break_off_radius: float = self.radius - ASTEROID_MIN_RADIUS

            asteroid_break_off_one = Asteroid(self.position[0], self.position[1], break_off_radius)
            asteroid_break_off_two = Asteroid(self.position[0], self.position[1], break_off_radius)

            asteroid_break_off_one.velocity = velosity_one * 1.2
            asteroid_break_off_two.velocity = velosity_two
