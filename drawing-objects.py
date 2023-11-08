# pylint: disable=no-member

# Import and initialize pygame
import pygame
# Get the clock
clock = pygame.time.Clock()

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

apple1 = GameObject(0, 250, 'apple.png')


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
  apple1.x += 2
  apple1.render(screen)

  # Update the window
  pygame.display.flip()
  clock.tick(60)

# Quit pygame when the loop exits
pygame.quit()
