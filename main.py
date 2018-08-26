#sys imports
import pygame, sys
import __builtin__
from pygame.locals import *

#custom imports
from ball import Ball
from bars import Bar
from colors import Colors
from sound import Sound

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
        width = 1920
        height = 1080
        __builtin__.windowSurface = pygame.display.set_mode((width, height), 0, 32)
        pygame.display.set_caption('Yet another PONG')        

        # load colors
        __builtin__.colors = Colors()
        __builtin__.mygame = self
        __builtin__.sounds = Sound()
        
        self.player1 = 0
        self.player2 = 0

        # set up fonts
        basicFont = pygame.font.SysFont(None, height/16)

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
        speed = 10
        self.bar1 = Bar(width/13, height/2, (speed*height)/768)
        self.bar2 = Bar(width*803/884, height/2, (speed*height)/768)
        self.ball = Ball(width*67/136, height*37/76)

    def updateScore(self):
        pygame.display.set_caption(str(self.player1) + ' - Yet another PONG - '+ str(self.player2))
    
    def runGameLoop(self):
        clock=pygame.time.Clock()
        # run the game loop
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            #erasing game objects
            self.bar1.erase()
            self.bar2.erase()
            self.ball.erase()
            
            #running game logic
            self.bar1.handle_keys(pygame.K_q, pygame.K_a)
            self.bar2.handle_keys(pygame.K_o, pygame.K_l)
            self.ball.move(self.bar1, self.bar2)
            
            #redrawing
            self.ball.draw()
            self.bar1.draw()
            self.bar2.draw()
            # upper bound
            w, h = pygame.display.get_surface().get_size() # get display width and height 
            pygame.draw.line(windowSurface, colors.WHITE, (0, h/15), (w, h/15), 5)
            
            #updating display
            pygame.display.update()
            clock.tick(60)

g = Game()
g.runGameLoop()
