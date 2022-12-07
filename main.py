import pygame, sys


pygame.init()
clock = pygame.time.Clock()

screenx,screeny = 1000,800

screen = pygame.display.set_mode([screenx,screeny])
pygame.display.set_caption("Cinematics")

vel = pygame.math.Vector2(0)
pos = pygame.math.Vector2(screenx/2, screeny/2)

endPoints = []

R, G, B = 255, 255, 255

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))

    mouse_pos = pygame.math.Vector2(pygame.mouse.get_pos())
    distance = mouse_pos - pos 

    acc = distance/10
    vel += acc/distance.magnitude()
    pos += vel

    endPoints.append((pos.x, pos.y))

    for i in range(len(endPoints) - 1):
            pygame.draw.line(screen, (R, G, B), (int(endPoints[i][0]), int(endPoints[i][1])), (int(endPoints[i + 1][0]), int(endPoints[i + 1][1])), 1)

    pygame.draw.circle(screen, (100,100,100), (pos.x, pos.y), 8)
    pygame.draw.line(screen, (0,255,0), pos, 10*vel+pos)
    pygame.draw.line(screen, (255,0,0), pos+vel*10, acc+10*vel+pos)

    font = pygame.font.SysFont("Comic Sans MS", 30)
    label_p = font.render("Position: " + str(pos), 1, (255,255,255))
    label_v = font.render("Velocity: " + str(vel), 1, (255,255,255))
    label_a = font.render("Acceleration: " + str(acc), 1, (255,255,255))

    screen.blit(label_p, (10,10))
    screen.blit(label_v, (10,30))
    screen.blit(label_a, (10,50))

    R -= 1
    G -= 1
    B -= 1

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
