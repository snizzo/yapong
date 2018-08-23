## here goes the code that renders and handles the ball

class Ball():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def draw(self, x, y):
        pygame.draw.circle(windowSurface, WHITE, [x, y], 15)
    
