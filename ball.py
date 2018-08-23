## here goes the code that renders and handles the ball

class Ball():
    def __init__(self, x, y):
        self.circle = pygame.circle.Circle((x, y, 15))
        
    def draw(self, surface):
        pygame.draw.circle(windowSurface, WHITE, self.circle)
    
