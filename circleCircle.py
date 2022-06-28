from fixedPoint import *
import numpy as np

def circleCircle(t1, t2, objectif):

    r1 = t1.dist(objectif)
    r2 = t2.dist(objectif)

    dx = t2.pos[0] - t1.pos[0]
    dy = t2.pos[1] - t1.pos[1]

    d = t1.dist(t2.pos)

    dx /= d
    dy /= d

    a = (r1 * r1 - r2 * r2 + d * d) / (2 * d)

    px = t1.pos[0] + (a * dx)
    py = t1.pos[1] + (a * dy)

    h = np.sqrt((r1 * r1) - (a * a))


    points = [
        [px + h * dy, py - h * dx],
        [px - h * dy, py + h * dx]
    ]

    return points

def distancePoints(p1, p2):
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)