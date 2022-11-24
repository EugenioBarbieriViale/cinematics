import pygame, sys


pygame.init()
clock = pygame.time.Clock()

screenx,screeny = 1000,800

window = pygame.display.set_mode([screenx,screeny])
pygame.display.set_caption("Cinematics")

vel = pygame.math.Vector2(0)
pos = pygame.math.Vector2(screenx/2, screeny/2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill((0,0,0))

    mouse_pos = pygame.math.Vector2(pygame.mouse.get_pos())
    distance = mouse_pos - pos 

    acc = distance/10
    vel += acc/distance.magnitude()
    pos += vel

    pygame.draw.circle(window, (100,100,100), (pos.x, pos.y), 8)
    pygame.draw.line(window, (0,255,0), pos, 10*vel+pos)
    pygame.draw.line(window, (255,0,0), pos+vel*10, acc+10*vel+pos)


    font = pygame.font.SysFont("Comic Sans MS", 30)
    # font = pygame.font.SysFont("monospace", 25)
    label_p = font.render("Position: " + str(pos), 1, (255,255,255))
    label_v = font.render("Velocity: " + str(vel), 1, (255,255,255))
    label_a = font.render("Acceleration: " + str(acc), 1, (255,255,255))

    window.blit(label_p, (10,10))
    window.blit(label_v, (10,30))
    window.blit(label_a, (10,50))

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
