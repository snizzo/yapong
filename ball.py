#sys imports
import pygame, sys
from pygame.locals import *

class Ball():
    def __init__(self, x, y):
        self.circle = pygame.draw.circle(windowSurface, colors.WHITE, (x, y), 10)
        
    def draw(self, surface):
        #pygame.draw.circle(windowSurface, colors.WHITE, self.circle)
        pass
    
