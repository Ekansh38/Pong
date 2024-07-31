import pygame
from pygame.math import Vector2


class Ball:
    def __init__(self, screen, size, speed):
        self.screen = screen
        self.radius = size
        self.speed = speed
        self.pos = Vector2(0, 0)
        self.vel = Vector2(0, 0)
        self.set_pos()
        self.set_vel()

    def set_pos(self):
        self.pos = Vector2(
            self.screen.get_width() / 2 - self.radius / 2,
            -10,
        )

    def set_vel(self):
        self.vel = Vector2(self.speed, self.speed)

    def draw(self):
        pygame.draw.ellipse(
            self.screen,
            "white",
            (self.pos.x, self.pos.y, self.radius, self.radius),
        )

    def check_bounds(self):
        if self.pos.y < 0:
            self.pos.y = 0
            self.vel.y *= -1
        elif self.pos.y > self.screen.get_height() - self.radius:
            self.pos.y = self.screen.get_height() - self.radius
            self.vel.y *= -1

    def check_score(self):
        if self.pos.x < 0:
            self.set_pos()
            self.set_vel()
            return 1
        elif self.pos.x > self.screen.get_width() - self.radius:
            self.set_pos()
            self.set_vel()
            return 2
        return 0

    def update(self):
        self.check_bounds()
        self.draw()
        self.pos += self.vel
        self.speed += 0.0009
