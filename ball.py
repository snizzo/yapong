#sys imports
import pygame, sys, math
from pygame.locals import *

class Ball(object):
    def __init__(self, x, y):
        self.speed = 2
        
        self.x = x
        self.y = y
        
        #starting direction
        self.cos = 1
        self.sin = 0.5
        self.rect = pygame.rect.Rect((x, y, 20, 20))
    
    def reset(self):
        self.speed = 4
        
        #starting direction
        self.cos = 1
        self.sin = 0.5
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
        if self.rect.y > 748: #basso
            self.cos = -self.cos
            self.increaseSpeed()
        if self.rect.y < 100: #alto
            self.cos = -self.cos
            self.increaseSpeed()
        if self.rect.x < 0: #sinistra
            self.reset()
            mygame.player2 += 1
            mygame.updateScore()
            sounds.playRandomWinSound()
        if self.rect.x > 1346: #destra
            self.reset()
            mygame.player1 += 1
            mygame.updateScore()
            sounds.playRandomWinSound()
    
    def increaseSpeed(self):
        if self.speed < 9:
            self.speed += 1
    
    def erase(self):
        pygame.draw.rect(windowSurface, colors.BLACK, self.rect)
    
    def draw(self):
        pygame.draw.rect(windowSurface, colors.WHITE, self.rect)
