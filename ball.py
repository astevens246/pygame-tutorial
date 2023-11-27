from random import randint, choice
import random
import pygame
from constants import lanes
from gameobject import GameObject

class Ball(GameObject):
    def __init__(self, ball_type):
        super(Ball, self).__init__(0, -64, f'{ball_type}.png', 50, 50)  
        self.dx = 0
        self.dy = randint(1, 2)  
        self.reset()
        print(f'{ball_type} Image Path: {self.image}')

    def move(self):
        self.rect.y += self.dy
        if self.rect.y > 500:
            self.reset()
        print(f'{self.__class__.__name__} Position: ({self.rect.x}, {self.rect.y})')

    def reset(self):
        self.rect.x = random.choice(lanes)
        self.rect.y = -64
        self.dy = randint(1, 2)

    def render(self, screen):
        print(f'{self.__class__.__name__} Rendering at: ({self.x}, {self.y})')
        super(Ball, self).render(screen)
