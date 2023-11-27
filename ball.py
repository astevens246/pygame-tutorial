# ball.py
from random import randint, choice
import random
import pygame
from gameobject import GameObject  # Update this import statement
from constants import lanes

class Ball(GameObject):
    def __init__(self, ball_type):
        super(Ball, self).__init__(0, -64, f'{ball_type}.png', 50, 50)
        self.dx = 0
        self.dy = randint(1, 2)
        self.ball_type = ball_type  # Add ball_type attribute
        self.reset()

    def move(self):
        self.rect.y += self.dy
        if self.rect.y > 500:
            self.reset()
        print(f'{self.__class__.__name__} Position: ({self.rect.x}, {self.rect.y})')

    def reset(self):
        self.rect.x = random.choice(lanes)
        self.rect.y = -64
        self.dy = randint(1, 2)
        return 40000000  # Add 40 million points when a fruit is collected

    def render(self, screen):
        print(f'{self.__class__.__name__} Rendering at: ({self.rect.x}, {self.rect.y})')
        super(Ball, self).render(screen)
