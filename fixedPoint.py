import numpy as np
import pygame

class tower:
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color

    def dist(self, obj):
        s = 0
        for i in range(len(obj)):
            s += (self.pos[i]-obj[i])**2
        return np.sqrt(s)

    def Draw(self, screen, obj=None):
        pygame.draw.circle(screen, (0,0,0), self.pos, 5)
        if obj:
            pygame.draw.circle(screen, self.color, self.pos, int(self.dist(obj)), 2)

    def intersections(self, other):
        d = self.dist(other.pos)
        a2b = [self.pos[i]-other.pos[i] for i in range(len(self.pos))]