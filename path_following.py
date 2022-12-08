import pygame, math, sys

pygame.init()
clock = pygame.time.Clock()

screenx,screeny = 1000,800

screen = pygame.display.set_mode([screenx,screeny])
pygame.display.set_caption("Path follower")

def draw_path():



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))

    draw_path()

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
