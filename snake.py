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

    '''    food = food_img.get_rect(x=ex_food.x, y = ex_food.y)
    screen.blit(food_img, food)'''

    def snake(self):
        snake_head = [self.x, self.y]
        self.snake_body.append(snake_head)
        for x in self.snake_body:
            if self.snake_body.index(x) == 0:
                tail_snake = tail_snake_img.get_rect(x=x[0], y = x[1])
                self.screen.blit(tail_snake_img, tail_snake)

            elif x == self.snake_body[-1]:
                head_snake = head_snake_img.get_rect(x=x[0], y = x[1])
                self.screen.blit(head_snake_img, head_snake)

            else:
                body_snake = body_snake_img.get_rect(x=x[0], y = x[1])
                self.screen.blit(body_snake_img, body_snake)


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