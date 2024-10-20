#!/usr/bin/env python3
import random
import sys

import pygame


def get_rgb_color(color_str):
    if color_str == "white":
        return (255, 255, 255)
    elif color_str == "black":
        return (0, 0, 0)
    else:
        raise Exception("Unknown color!")


def play_game(screen, width, height):
    # Initialize variables used in game
    paddle_x = 100
    paddle_y = height // 2

    ball_x_speed = random.randint(2, 4)
    ball_y_speed = 0

    ball_x = width // 2
    ball_y = height // 2

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get user input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            paddle_y = paddle_y - 5

        # Move non-player characters
        ball_x += ball_x_speed
        ball_y += ball_y_speed

        # Check for collisions
        if ball_x >= width:
            ball_x_speed = -1 * ball_x_speed

        # Draw paddles/ball in proper position
        screen.fill(get_rgb_color("black"))
        pygame.draw.rect(screen, get_rgb_color("white"), (paddle_x, paddle_y, 20, 80))
        pygame.draw.circle(screen, get_rgb_color("white"), (ball_x, ball_y), 10)
        pygame.display.flip()
        pygame.time.delay(10)


# Main "hook"
if __name__ == "__main__":
    print("Welcome to pong!!! Let's get started!")
    pygame.init()

    # Set up the game window
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pong")

    play_game(screen, width, height)
