## here goes the code that renders and handles the bars

class Bar():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def draw(self, x, y):
        pygame.draw.rect(windowSurface, WHITE, [x, y, 20, 100])
    
