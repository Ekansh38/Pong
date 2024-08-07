import pygame
from pygame.math import Vector2

from ball import Ball
from paddle import Paddle

# YESS

# Constants
SCREEN_SIZE = Vector2(1236, 844)
FPS = 60
TITLE = "Pong"
WINNING_SCORE = 10

# Pygame setup
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
running = True

ball = Ball(screen, 20, 6)
paddle_left = Paddle(screen, "left", 8, ball)
paddle_right = Paddle(screen, "right", 8, ball)
left_score = 0
right_score = 0

# Draw the score
font = pygame.font.Font(None, 74)

game_over = False
winner = None

# Game Loop
while running:
    screen.fill("black")
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.line(
        screen, "white", (SCREEN_SIZE.x / 2, 0), (SCREEN_SIZE.x / 2, SCREEN_SIZE.y), 5
    )

    if not game_over:
        paddle_left.update()
        paddle_right.update()
        ball.update()

        score = ball.check_score()
        if score == 1:
            right_score += 1
        elif score == 2:
            left_score += 1

        if left_score >= WINNING_SCORE:
            game_over = True
            winner = "HUMAN"
        elif right_score >= WINNING_SCORE:
            game_over = True
            winner = "AI"

    # Draw the score
    left_score_text = font.render(str(left_score), True, "white")
    right_score_text = font.render(str(right_score), True, "white")
    screen.blit(left_score_text, (SCREEN_SIZE.x / 4, 50))
    screen.blit(right_score_text, (3 * SCREEN_SIZE.x / 4, 50))

    if game_over:
        game_over_text = font.render(f"GAME OVER, {winner} WINS", True, "white")
        text_rect = game_over_text.get_rect(
            center=(SCREEN_SIZE.x / 2, SCREEN_SIZE.y / 2)
        )
        screen.blit(game_over_text, text_rect)

    pygame.display.update()

pygame.quit()
