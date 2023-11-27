# ball.py
from random import randint, choice
import random
import pygame
from gameobject import GameObject
from constants import lanes

class Ball(GameObject):
    def __init__(self, ball_type):
        super(Ball, self).__init__(0, -64, f'{ball_type}.png', 50, 50)
        self.dx = 0
        self.dy = randint(1, 2)
        self.ball_type = ball_type

        self.reset()

    def move(self):
        self.rect.y += self.dy
        if self.rect.y > 500:
            self.reset()

    def reset(self):
        self.rect.x = random.choice(lanes)
        self.rect.y = -64
        self.dy = randint(1, 2)
        if self.ball_type == 'bomb_ball':
            return 0
        else:
            return 100 

    def render(self, screen):
        super(Ball, self).render(screen)

    def get_radius(self):
        # Return the radius of the circular hitbox
        return self.rect.width // 2
