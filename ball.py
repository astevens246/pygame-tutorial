# ball.py
from random import randint, choice
import pygame
from gameobject import GameObject
from constants import lanes

class Ball(GameObject):
    def __init__(self, ball_type, fruit_image=None):
        super(Ball, self).__init__(0, -64, fruit_image, 50, 50)
        self.dx = 0
        self.dy = randint(1, 2)
        self.ball_type = ball_type

        self.reset()

    def move(self):
        self.rect.y += self.dy
        if self.rect.y > 500:
            self.reset()

    def reset(self):
        self.rect.x = choice(lanes)
        self.rect.y = -64
        self.dy = randint(1, 2)
        return 1  # Return 1 to indicate a successful reset

    def render(self, screen):
        super(Ball, self).render(screen)

    def update(self):
        self.move()
        # Add any other update logic for the ball
