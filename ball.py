## here goes the code that renders and handles the ball

class Ball():
    def __init__(self, x, y):
        self.circle = pygame.circle.Circle((x, y, 15))
        
    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 1
        if key[pygame.K_LEFT]:
           self.circle.move_ip(-1, 0)
        if key[pygame.K_RIGHT]:
           self.circle.move_ip(1, 0)
        if key[pygame.K_UP]:
           self.circle.move_ip(0, -1)
        if key[pygame.K_DOWN]:
           self.circle.move_ip(0, 1)
        
    def draw(self, surface):
        pygame.draw.circle(windowSurface, WHITE, self.circle)
    
