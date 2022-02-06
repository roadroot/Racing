import pygame

from car import car

(width, height) = (720, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Race')
background_colour = (255,255,255)
# all_sprites = pygame.sprite.Group()
# all_sprites.update()
# all_sprites.draw(screen)
carImg = pygame.image.load('resource/car.png')
carImg = pygame.transform.scale(carImg, (carImg.get_size()[0]*0.5, carImg.get_size()[1]*0.5))
def renderCarAt(x,y):
    screen.blit(carImg, (x,y))
c = car()
pygame.display.flip()
running = True
x=0
while running:
  x += 1
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      keys=pygame.key.get_pressed()
      if keys[pygame.K_UP]:
        c.accelerate()
    screen.fill(background_colour)
    renderCarAt(c.position[0], c.position[1])
    pygame.display.update()

