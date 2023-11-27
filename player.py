# player.py
import pygame
from gameobject import GameObject

class Player(GameObject):
    def __init__(self):
        super(Player, self).__init__(0, 0, 'player.png', 50, 50)
        self.dx = 0
        self.dy = 0
        self.reset()

    def left(self):
        self.dx -= 20

    def right(self):
        self.dx += 20

    def up(self):
        self.dy -= 20

    def down(self):
        self.dy += 20

    def move(self):
        self.rect.x -= (self.rect.x - self.dx) * 0.25
        self.rect.y -= (self.rect.y - self.dy) * 0.25

        # Restrict the player's position to stay within the screen boundaries
        self.x = max(0, min(self.x, 500 - self.image.get_width()))
        self.y = max(0, min(self.y, 500 - self.image.get_height()))

    def reset(self):
        self.x = 250 - 32
        self.y = 250 - 32
        self.dx = 0
        self.dy = 0

    def render(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def get_radius(self):
        # Return the radius of the circular hitbox
        return self.rect.width // 2
