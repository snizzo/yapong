#sys imports
import pygame, sys
from pygame.locals import *

class Bar(object):
    def __init__(self, x, y, speed):
        self.speed = speed
        self.rect = pygame.rect.Rect((x, y, 20, 100))
        self.draw()
    
    #getters/setters    
    def getRect(self):
        return self.rect
    
    #logic
    def handle_keys(self, key_up, key_down):
        key = pygame.key.get_pressed()
        dist = 1
        if key[key_up]:
            if self.rect.y > 110:
                self.rect.move_ip(0, -1*self.speed)
        if key[key_down]:
            if self.rect.y < 665:
                self.rect.move_ip(0, 1*self.speed)
    
    def erase(self):
        pygame.draw.rect(windowSurface, colors.BLACK, self.rect)
    
    def draw(self):
        pygame.draw.rect(windowSurface, colors.WHITE, self.rect)
    
