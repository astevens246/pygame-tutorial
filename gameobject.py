import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image, width=None, height=None):
        super(GameObject, self).__init__()
        self.image = pygame.image.load(image)  # Load image
        if width and height:
            self.image = pygame.transform.scale(self.image, (width, height))  # Resize image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.x = x
        self.y = y

    def render(self, screen):
        screen.blit(self.image, self.rect.topleft)
