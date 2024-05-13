'''Создать прямоугольник с тенью. Тень должна находиться под наклоном. . 
Прямоугольник с тенью должны двигаться при нажатии на кнопки клавиатуры W, A, S, D.'''

import pygame
import sys
from settings import *
from snake import Snake
from food import Food
import random
from modules.menu import Menu
from modules.reset import reset
from modules.display_score import display_score



pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")


ex_food = Food(HEIGHT, WIDTH)
snake = Snake(pygame, screen)
snake2 = Snake(pygame, screen)

snake2.x = 100
snake2.y = 100

Menu('main').launch(screen)
bg.play(loops=1)
bg.set_volume(0.3)
def draw():
    screen.fill(BLACK) 
    food = food_img.get_rect(x=ex_food.x, y = ex_food.y)
    screen.blit(food_img, food)
    if food.x + SIZE > snake.x > food.x - SIZE and food.y + SIZE > snake.y > food.y - SIZE:
        ex_food.x = random.randrange(0, WIDTH, 5)
        ex_food.y = random.randrange(0, HEIGHT, 5) 
        snake.length += 1
        eat.play()

    snake.snake(vector)

    display_score(screen, 2)

    for i in snake.snake_body[:-1]:
        if i == [snake.x, snake.y]:
            bg.stop()
            game_over.play()
            snake.length = reset(screen ,snake.length)
            bg.play()
    

    pygame.display.update()

while True:
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if vector != 's':
                    vector = 'w'
            elif event.key == pygame.K_s:
                if vector != 'w':
                    vector = 's'
            elif event.key == pygame.K_a:
                if vector != 'd':
                    vector = 'a'
            elif event.key == pygame.K_d:
                if vector != 'a':
                    vector = 'd'
            elif event.key == pygame.K_m:
                Menu('pause').launch(screen)

    pygame.time.Clock().tick(FPS)