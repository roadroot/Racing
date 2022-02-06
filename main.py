import pygame

(width, height) = (720, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Race')
background_colour = (255,255,255)
screen.fill(background_colour)
all_sprites = pygame.sprite.Group()
all_sprites.update()
all_sprites.draw(screen)
pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
