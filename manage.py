'''Создать прямоугольник с тенью. Тень должна находиться под наклоном. . 
Прямоугольник с тенью должны двигаться при нажатии на кнопки клавиатуры W, A, S, D.'''

import pygame
import sys
from settings import *
from snake import Snake
from food import Food
import random
from menu import menu
from reset import reset



pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")


ex_food = Food(HEIGHT, WIDTH)
snake = Snake(pygame, screen)
menu.main_menu().mainloop(screen)

def draw():
    screen.fill(BLACK) 
    food = pygame.draw.rect(screen, RED, (ex_food.x, ex_food.y, 20, 20))
    if food.x + 20 > snake.x > food.x - 20 and food.y + 20 > snake.y > food.y - 20:
        ex_food.x = random.randrange(0, WIDTH, 5)
        ex_food.y = random.randrange(0, HEIGHT, 5) 
        snake.length += 1
        
    snake.bord()
    snake.snake()
    snake.move(vector)

    font_style = pygame.font.SysFont("Arial",size=25)
    mes = font_style.render(f'Очки: {snake.length - 1}', True, WHITE)
    screen.blit(mes, [10,10])

    for i in snake.snake_body[:-1]:
        if i == [snake.x, snake.y]:
            snake.length = reset(screen ,snake.length)
    

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
                menu.main_menu().mainloop(screen)

    pygame.time.Clock().tick(FPS)