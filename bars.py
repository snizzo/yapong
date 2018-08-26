#sys imports
import pygame, sys
from pygame.locals import *

class Bar(object):
    def __init__(self, x, y, speed):
        self.speed = speed
        w, h = pygame.display.get_surface().get_size() 
        self.rect = pygame.rect.Rect((x, y, w/68, h/7))
        self.draw()
    
    #getters/setters    
    def getRect(self):
        return self.rect
    
    #logic
    def handle_keys(self, key_up, key_down):
        key = pygame.key.get_pressed()
        dist = 1
        w, h = pygame.display.get_surface().get_size()
        if key[key_up]:
            if self.rect.y > (h/15)+10:
                self.rect.move_ip(0, -1*self.speed)
        if key[key_down]:
            if self.rect.y < (6*h/7)-5:
                self.rect.move_ip(0, 1*self.speed)
    
    def erase(self):
        pygame.draw.rect(windowSurface, colors.BLACK, self.rect)
    
    def draw(self):
        pygame.draw.rect(windowSurface, colors.WHITE, self.rect)
    
