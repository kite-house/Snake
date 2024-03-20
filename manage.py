'''Создать прямоугольник с тенью. Тень должна находиться под наклоном. . 
Прямоугольник с тенью должны двигаться при нажатии на кнопки клавиатуры W, A, S, D.'''

import pygame
import sys
from settings import *
from snake import Snake
from food import Food
import random

pygame.init()

food1 = Food(HEIGHT, WIDTH)
vector = None
screen = pygame.display.set_mode((WIDTH, HEIGHT))
snake = Snake(WIDTH, HEIGHT)
def draw():
    screen.fill(BLACK) 
    food = pygame.draw.rect(screen, RED, (food1.x, food1.y, 20, 20))
    if food.x + 20 > snake.x > food.x - 20 and food.y + 20 > snake.y > food.y - 20 :
        print('ВЫ ПОЛУЧАЕТЕ ОЧКИ')
        food1.x = random.randrange(0, WIDTH, 5)
        food1.y = random.randrange(0, HEIGHT, 5) 
        snake.add_snake()

    snake.snake(pygame, screen, GREEN, vector)
    snake.move(vector)
    pygame.display.update()

while True:
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                vector = 'w'
            elif event.key == pygame.K_s:
                vector = 's'
            elif event.key == pygame.K_a:
                vector = 'a'
            elif event.key == pygame.K_d:
                vector = 'd'
                
    pygame.time.Clock().tick(FPS)