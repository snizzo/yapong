#sys imports
import pygame, sys
import __builtin__
from pygame.locals import *

#custom imports
from ball import Ball
from bars import Bar
from colors import Colors

class Game():
    def __init__(self):
        #building initial scene
        self.setupGame()
        
        # draw the window onto the screen
        pygame.display.update()
    
    def setupGame(self):
        # set up pygame
        pygame.init()

        # set up the window
        __builtin__.windowSurface = pygame.display.set_mode((1366, 768), 0, 32)
        pygame.display.set_caption('Yet another PONG')        

        # load colors
        __builtin__.colors = Colors()

        # set up fonts
        basicFont = pygame.font.SysFont(None, 48)

        # set up the text
        text = basicFont.render('Yet another PONG!', False, colors.WHITE, colors.BLACK)
        textRect = text.get_rect()
        textRect.centerx = windowSurface.get_rect().centerx
        textRect.y = 12
        #textRect.centery = windowSurface.get_rect().centery

        # draw the white background onto the surface
        windowSurface.fill(colors.BLACK)

        # draw the text's background rectangle onto the surface
        pygame.draw.rect(windowSurface, colors.WHITE, (textRect.left - 3, textRect.top - 3, textRect.width + 6, textRect.height + 6))

        # draw the text onto the surface
        windowSurface.blit(text, textRect)
        
        #example of ball and bar class
        self.bar1 = Bar(0,0)
        self.bar2 = Bar(100,100)
        self.ball = Ball(300,300)

    
    def runGameLoop(self):
        # run the game loop
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.bar1.handle_keys()
            self.bar2.handle_keys()

g = Game()
g.runGameLoop()
