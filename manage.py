import pygame
import sys
from settings import *
from entities.snake import Snake
from entities.food import Food
from modules.menu import Menu
from modules.display_score import display_score

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")


food = Food()
snake = Snake(pygame, screen)

Menu('main').launch(screen)

bg.play(loops=1)
bg.set_volume(0.3)

def draw():
    screen.fill(BLACK) 
    food.create(screen, snake)
    snake.snake(vector)
    display_score(screen, snake.length-1)
    pygame.display.update()

while True:
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if vector != 's' or snake.length == 1:
                    vector = 'w'
                    
            elif event.key == pygame.K_s:
                if vector != 'w' or snake.length == 1:
                    vector = 's'

            elif event.key == pygame.K_a:
                if vector != 'd' or snake.length == 1:
                    vector = 'a'

            elif event.key == pygame.K_d:
                if vector != 'a' or snake.length == 1:
                    vector = 'd'

            elif event.key == pygame.K_m:
                Menu('pause').launch(screen)

    pygame.time.Clock().tick(FPS)