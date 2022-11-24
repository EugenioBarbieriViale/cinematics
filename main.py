import pygame, sys

pygame.init()
clock = pygame.time.Clock()

screenx,screeny = 1000,800

window = pygame.display.set_mode([screenx,screeny])
pygame.display.set_caption("Gravity simulator")

x = screenx//2
y = screeny//2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill((0,0,0))


    pygame.draw.circle(window, (100,100,100), (x,y), 8)

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
