import pygame, sys
import math

pygame.init()
clock = pygame.time.Clock()

screenx,screeny = 1000,800

screen = pygame.display.set_mode([screenx,screeny])
pygame.display.set_caption("Cinematics")


a = 300
b = 300

e = math.sqrt(a**2 - b**2)/a
p = b**2/a

pos = pygame.Vector2(200,200)
fire = pygame.Vector2(screenx//2,screeny//2)

theta = 0

endPoints = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))

    ang_acc = 
    ang_vel =
    theta += 0.1

    r = p/(1 + e*math.cos(theta))

    pos.x = r * math.cos(theta) + fire.x
    pos.y = r * math.sin(theta) + fire.y
    endPoints.append((pos.x, pos.y))

    for i in range(len(endPoints) - 1):
            pygame.draw.line(screen, (255, 255, 255), (int(endPoints[i][0]), int(endPoints[i][1])), (int(endPoints[i + 1][0]), int(endPoints[i + 1][1])), 1)

    if theta == init_theta*count:
        endPoints = []

    pygame.draw.circle(screen, (255,0,0), fire, 5)
    pygame.draw.circle(screen, (100,100,100), pos, 8)
    # pygame.draw.line(screen, (0,255,0), pos, 10*vel+pos)
    # pygame.draw.line(screen, (255,0,0), pos+vel*10, acc+10*vel+pos)

    # font = pygame.font.SysFont("Comic Sans MS", 30)
    # label_p = font.render("Position: " + str(pos), 1, (255,255,255))
    # label_v = font.render("Velocity: " + str(vel), 1, (255,255,255))
    # label_a = font.render("Acceleration: " + str(acc), 1, (255,255,255))

    # screen.blit(label_p, (10,10))
    # screen.blit(label_v, (10,30))
    # screen.blit(label_a, (10,50))

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
