#sys imports
import pygame, sys, random
import __builtin__
from pygame.locals import *

class Sound():
    def __init__(self):
        self.wins = []
        self.wins.append(pygame.mixer.Sound("sfx/win1.ogg"))
        self.wins.append(pygame.mixer.Sound("sfx/win2.ogg"))
        self.wins.append(pygame.mixer.Sound("sfx/win3.ogg"))
        self.wins.append(pygame.mixer.Sound("sfx/win4.ogg"))
        self.wins.append(pygame.mixer.Sound("sfx/win5.ogg"))
        self.wins.append(pygame.mixer.Sound("sfx/win6.ogg"))
    
    def playRandomWinSound(self):
        r = int(random.uniform(0,6))
        print r
        self.wins[r].play()
