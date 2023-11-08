# pylint: disable=no-member

# Import and initialize pygame
import pygame

class GameObject(pygame.sprite.Sprite):
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    self.surf = pygame.image.load(image) #add image
    self.x = x
    self.y = y
  
  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))

pygame.init()

  
# Configure the screen
screen = pygame.display.set_mode([500, 500])

apple1 = GameObject(0, 0, 'apple.png')
apple2 = GameObject(450, 0, 'apple.png')
apple3 = GameObject(200, 200, 'apple.png')
apple4 = GameObject(450, 450, 'apple.png')
apple5 = GameObject(0, 450, 'apple.png')

strawberry1 = GameObject(245, 0, 'strawberry.png')
strawberry2 = GameObject(0, 245, 'strawberry.png')
strawberry3 = GameObject(450, 245, 'strawberry.png')
strawberry4 = GameObject(245, 450, 'strawberry.png')


# Create the game loop
running = True
while running:
  # Look at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      # Clear screen
  screen.fill((0, 0, 0))

  # Draw the box object
  apple1.render(screen)
  apple2.render(screen)
  apple3.render(screen)
  apple4.render(screen)
  apple5.render(screen)

  strawberry1.render(screen)
  strawberry2.render(screen)
  strawberry3.render(screen)
  strawberry4.render(screen)

  # Update the window
  pygame.display.flip()

# Quit pygame when the loop exits
pygame.quit()
