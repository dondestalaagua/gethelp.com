import pygame

pygame.init()
screen = pygame.display.set_mode((300,
200))
pygame.display.set_caption("Soy la 69")
clock = pygame.time.Clock()
test_surface = pygame.Surface((100,200))
test_surface.fill('Red')
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
  screen.blit(test_surface, (200,000)
                             
  clock.tick(60)
  pygame.display.update()


