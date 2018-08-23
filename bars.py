## here goes the code that renders and handles the bars

class Bar():
    def __init__(self, x, y):
        self.rect = pygame.rect.Rect((x, y, 20, 100))
        
    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 1
        if key[pygame.K_LEFT]:
           self.rect.move_ip(-1, 0)
        if key[pygame.K_RIGHT]:
           self.rect.move_ip(1, 0)
        if key[pygame.K_UP]:
           self.rect.move_ip(0, -1)
        if key[pygame.K_DOWN]:
           self.rect.move_ip(0, 1)
        
    def draw(self, surface):
        pygame.draw.rect(windowSurface, WHITE, self.rect)
    
