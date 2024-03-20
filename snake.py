import time

class Snake:
    def __init__(self, WIDTH, HEIGHT):
        self.y = HEIGHT // 2
        self.x = WIDTH // 2
        self.length = 1

    def move(self, vector):
        if vector == 'w':
            self.y -= 5

        elif vector == 's':
            self.y += 5

        elif vector == 'a':
            self.x -= 5

        elif vector == 'd':
            self.x += 5

    def add_snake(self):
        self.length += 1

    def snake(self, pygame, screen, GREEN, vector):
        for i in range(self.length):
            if vector == 'w':
                pygame.draw.rect(screen, GREEN, (self.x, self.y - i * 21, 20, 20))
            elif vector == 's':
                pygame.draw.rect(screen, GREEN, (self.x, self.y + i * 21, 20, 20))
            elif vector == 'a':
                pygame.draw.rect(screen, GREEN, (self.x - i * 21, self.y, 20, 20))

            elif vector == 'd':
                pygame.draw.rect(screen, GREEN, (self.x + i * 21, self.y, 20, 20))
            time.sleep(0.001)