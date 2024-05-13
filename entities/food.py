import random
from settings import *

class Food():
    def __init__(self):
        self.y = random.randrange(10, HEIGHT - 10, 5)
        self.x = random.randrange(10, WIDTH - 10, 5)
 
    def create(self, screen, snake):
        self.food = food_img.get_rect(x=self.x, y = self.y)
        screen.blit(food_img, self.food)
        self.reset(snake)

    def reset(self,snake):
        if self.food.x + SIZE > snake.x > self.food.x - SIZE and self.food.y + SIZE > snake.y > self.food.y - SIZE:
            self.x = random.randrange(0, WIDTH, 5)
            self.y = random.randrange(0, HEIGHT, 5) 
            snake.length += 1
            eat.play()