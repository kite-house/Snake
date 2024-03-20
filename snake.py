from settings import *

class Snake:
    def __init__(self, pygame, screen):
        self.y = HEIGHT // 2
        self.x = WIDTH // 2
        self.length = 1
        self.snake_body = []

        self.pygame = pygame
        self.screen = screen

    def move(self, vector):
        if vector == 'w':
            self.y -= 5

        elif vector == 's':
            self.y += 5

        elif vector == 'a':
            self.x -= 5

        elif vector == 'd':
            self.x += 5

    def snake(self):
        snake_head = [self.x, self.y]
        self.snake_body.append(snake_head)
        for x in self.snake_body:
            self.pygame.draw.rect(self.screen, GREEN, [x[0], x[1], 20, 20])
            if len(self.snake_body) > self.length: 
                del self.snake_body[0]   

        for x in self.snake_body[:-1]:
            if x == snake_head:
                print('проигр')


    def bord(self):
        if self.x > WIDTH:
            self.x = 0

        elif self.x < 0:
            self.x = WIDTH

        elif self.y > HEIGHT:
            self.y = 0

        elif self.y < 0:
            self.y = HEIGHT