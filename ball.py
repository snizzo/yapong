#sys imports
import pygame, sys, math, random
from pygame.locals import *

class Ball(object):
    def __init__(self, x, y):
        self.speed = 2
        
        self.x = x
        self.y = y
        
        #starting direction
        self.cos = 1
        self.sin = 0.5
        w, h = pygame.display.get_surface().get_size()
        self.rect = pygame.rect.Rect((x, y, w/68, w/68))
    
    def reset(self, sin, cos):
        
        self.speed = 4
        
        #starting direction
        self.cos = cos
        self.sin = sin
        self.rect.x = self.x
        self.rect.y = self.y
    
    def move(self, bar1, bar2):
        self.rect.move_ip(self.sin*self.speed*3, self.cos*self.speed)
        
        #bars
        if self.rect.colliderect(bar1.getRect()):
            self.increaseSpeed()
            self.sin = -self.sin
            
            offset = (self.rect.y + 10) - (bar1.getRect().y + 50)
            self.cos = offset/50.0
        
        if self.rect.colliderect(bar2.getRect()):
            self.increaseSpeed()
            self.sin = -self.sin
            offset = (self.rect.y + 10) - (bar2.getRect().y + 50)
            self.cos = offset/50.0
        
        #window borders
        w, h = pygame.display.get_surface().get_size()
        
        if self.rect.y > h-(w/68)-5: #basso
            self.cos = -self.cos
            self.increaseSpeed()
        if self.rect.y < (h/15)+10: #alto
            self.cos = -self.cos
            self.increaseSpeed()
        if self.rect.x < 0: #sinistra
            r = random.uniform(0,1)
            mygame.player2 += 1
            mygame.updateScore()
            sounds.playRandomWinSound()
            self.reset(1, r)
        if self.rect.x > w: #destra
            r = random.uniform(0,1)
            mygame.player1 += 1
            mygame.updateScore()
            sounds.playRandomWinSound()
            self.reset(-1, r)
    
    def increaseSpeed(self):
        if self.speed < 9:
            self.speed += 1
    
    def erase(self):
        pygame.draw.rect(windowSurface, colors.BLACK, self.rect)
    
    def draw(self):
        pygame.draw.rect(windowSurface, colors.WHITE, self.rect)
