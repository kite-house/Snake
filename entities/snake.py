from settings import *
from modules.reset import reset
class Snake:
    def __init__(self, pygame, screen):
        self.y = HEIGHT // 2
        self.x = WIDTH // 2
        self.length = 1
        self.snake_body = []
        self.turn = 0

        self.pygame = pygame
        self.screen = screen

    def move(self, vector):
        if vector == 'w':
            self.y -= 5
            self.turn = 3

        elif vector == 's':
            self.y += 5
            self.turn = 0

        elif vector == 'a':
            self.x -= 5
            self.turn = 1

        elif vector == 'd':
            self.x += 5
            self.turn = 2

    def snake(self, vector):
        snake_head = [self.x, self.y]
        self.snake_body.append(snake_head)
        for x in self.snake_body:
            if self.snake_body.index(x) == 0 and self.length > 2:
                tail_snake_rect = tail_snake[self.turn].get_rect(x=x[0], y = x[1])
                self.screen.blit(tail_snake[self.turn], tail_snake_rect)

            elif x == self.snake_body[-1] or self.length == 1:
                head_snake_rect = head_snake[self.turn].get_rect(x=x[0], y = x[1])
                self.screen.blit(head_snake[self.turn], head_snake_rect)

            else:
                body_snake_rect = body_snake.get_rect(x=x[0], y = x[1])
                self.screen.blit(body_snake, body_snake_rect)


            if len(self.snake_body) > self.length: 
                del self.snake_body[0]   
        
        self.bord()
        self.move(vector)
        self.gameover()

    def bord(self):
        if self.x > WIDTH:
            self.x = 0

        elif self.x < 0:
            self.x = WIDTH

        elif self.y > HEIGHT:
            self.y = 0

        elif self.y < 0:
            self.y = HEIGHT

    def gameover(self):
        for i in self.snake_body[:-1]:
            if i == [self.x, self.y]:
                bg.stop()
                game_over.play()
                self.length = reset(self.screen)
                bg.play()
        