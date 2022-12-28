import pygame, sys
import math

pygame.init()
clock = pygame.time.Clock()

screenx,screeny = 800,600

screen = pygame.display.set_mode([screenx,screeny])
pygame.display.set_caption("Cinematics")

pos = pygame.Vector2(200, 200)
vel = pygame.Vector2(0)


centre = pygame.Vector2(screenx//2, screeny//2)
r = 200

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))

    direction = pygame.math.Vector2(pos - centre) # acc

    acc = 0.01*direction
    vel = vel + acc
    pos -= vel

    pygame.draw.circle(screen, (255,255,255), centre, 7)
    pygame.draw.circle(screen, (255,255,255), pos, 7)
    #pygame.draw.circle(screen, (255,0,0), centre, r, width=3)

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()