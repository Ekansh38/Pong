import time

import pygame
from pygame.math import Vector2


class Paddle:
    def __init__(self, screen, side, speed, ball):
        self.screen = screen
        self.side = side
        self.speed = speed
        self.width = 20
        self.height = 100
        self.pos = Vector2(0, 0)
        self.ball = ball
        self.set_pos()

    def update(self):
        self.check_input()
        self.draw()
        self.check_bounds()
        self.ball_collision()
        self.speed += 0.002

    def ball_collision(self):
        if self.side == "left":
            if (
                self.ball.pos.x <= self.pos.x + self.width
                and self.ball.pos.y > self.pos.y
                and self.ball.pos.y < self.pos.y + self.height
            ):
                self.ball.vel.x *= -1
        elif self.side == "right":
            if (
                self.ball.pos.x + self.ball.radius >= self.pos.x - 5
                and self.ball.pos.y > self.pos.y
                and self.ball.pos.y < self.pos.y + self.height
            ):
                self.ball.vel.x *= -1

    def check_bounds(self):
        if self.pos.y < 0:
            self.pos.y = 0
        elif self.pos.y > self.screen.get_height() - self.height:
            self.pos.y = self.screen.get_height() - self.height

    def set_pos(self):
        margin = -9
        if self.side == "left":
            self.pos = Vector2(margin, self.screen.get_height() / 2 - self.height / 2)
        elif self.side == "right":
            self.pos = Vector2(
                self.screen.get_width() - margin - self.width,
                self.screen.get_height() / 2 - self.height / 2,
            )

    def check_input(self):
        keys = pygame.key.get_pressed()
        if self.side == "left":
            if keys[pygame.K_w]:
                self.pos.y -= self.speed
            if keys[pygame.K_s]:
                self.pos.y += self.speed
        elif self.side == "right":
            MAX_MOVEMENT = self.speed
            MOVEMENT_COOLDOWN = 0.05  # Seconds between movements
            DEADZONE = 15
            SMOOTHING_FACTOR = 0.2  # Adjust this value between 0 and 1

            last_movement_time = 0

            while True:
                f_x = self.ball.pos.x
                f_y = self.ball.pos.y
                new_vel = Vector2(self.ball.vel.x, self.ball.vel.y)
                while True:
                    if f_y < 0 or f_y > self.screen.get_height():
                        new_vel.y *= -1
                    if f_x < 0:
                        new_vel.x *= -1
                    if f_x >= self.pos.x:
                        break
                    f_x += new_vel.x
                    f_y += new_vel.y

                diff = f_y - (self.pos.y + self.height // 2)
                current_time = time.time()

                if abs(diff) < DEADZONE:
                    break
                elif current_time - last_movement_time >= MOVEMENT_COOLDOWN:
                    movement = diff * SMOOTHING_FACTOR
                    movement = max(
                        min(movement, MAX_MOVEMENT), -MAX_MOVEMENT
                    )  # Limit movement
                    self.pos.y += movement
                    last_movement_time = current_time
                    break

    def draw(self):
        pygame.draw.rect(
            self.screen,
            "white",
            (self.pos.x, self.pos.y, self.width, self.height),
        )
