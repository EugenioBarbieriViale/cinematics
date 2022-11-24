import pygame, sys

pygame.init()
clock = pygame.time.Clock()

screenx,screeny = 1000,800

window = pygame.display.set_mode([screenx,screeny])
pygame.display.set_caption("Gravity simulator")

vel = pygame.math.Vector2(0)
obj_pos = pygame.math.Vector2(screenx/2, screeny/2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill((0,0,0))

    mouse_pos = pygame.math.Vector2(pygame.mouse.get_pos())
    distance = mouse_pos - obj_pos 

    acc = distance/10
    vel += acc/distance.magnitude()
    obj_pos += vel

    pygame.draw.circle(window, (100,100,100), (obj_pos.x, obj_pos.y), 8)
    pygame.draw.line(window, (0,255,0), obj_pos, 10*vel+obj_pos)
    pygame.draw.line(window, (255,0,0), obj_pos+vel*10, acc+10*vel+obj_pos)

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
