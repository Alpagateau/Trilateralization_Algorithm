import numpy as np
import pygame
from fixedPoint import *
from circleCircle import *

def calculatePoint(screen,t1, t2, t3, objectif):

    r1 = t1.dist(objectif)
    r2 = t2.dist(objectif)
    r3 = t3.dist(objectif)

    points = circleCircle(t1, t2, objectif)
    points2 = circleCircle(t1, t3, objectif)

    dists =[
        distancePoints(points[0], points2[0]),
        distancePoints(points[0], points2[1]),
        distancePoints(points[1], points2[0]),
        distancePoints(points[1], points2[1])
    ]

    minD = dists.index(np.min(dists))

    pygame.draw.line(screen, (255,255,255), points[0], points[1])

    if minD == 0:
        return [points[0][0], points2[0][1]]
    elif minD == 1:
        return [points[0][0], points2[1][1]]
    elif minD == 2:
        return [points[1][0], points2[0][1]]
    elif minD == 3:
        return [points[1][0], points2[1][1]]
    else:
        return [0,0]


background_colour = (255,255,255)
(width, height) = (500, 500)

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('GPS Test')


screen.fill(background_colour)

t = tower([400,400], (100,100,100))
d = tower([75,30], (150,150,150))
e = tower([60,300], (200,200,200))

objectif = [150,150]

pygame.display.flip()

running = True
while running:
    pygame.display.flip()
    screen.fill(background_colour)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    t.Draw(screen, objectif)
    d.Draw(screen, objectif)
    e.Draw(screen, objectif)

    res = calculatePoint(screen, t, d, e, objectif)

    objectif = pygame.mouse.get_pos()
    pygame.draw.circle(screen, (255,0,0), objectif, 7)
    pygame.draw.circle(screen, (0,255,0), res, 3)
