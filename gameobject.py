# gameobject.py
import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image, width=None, height=None):
        super(GameObject, self).__init__()
        self.image = pygame.image.load(image)
        if width and height:
            self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))

    def render(self, screen):
        screen.blit(self.image, self.rect.topleft)