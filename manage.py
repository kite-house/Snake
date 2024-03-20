'''Создать прямоугольник с тенью. Тень должна находиться под наклоном. . 
Прямоугольник с тенью должны двигаться при нажатии на кнопки клавиатуры W, A, S, D.'''

import pygame
import sys
from settings import *

pygame.init()


screen = pygame.display.set_mode((800, 600))


rect_width = 100
rect_height = 50
rect_x = 350
rect_y = 250
shadow_offset = 10

def draw():
    screen.fill(BLACK)
    shadow_rect = pygame.Rect(rect_x + shadow_offset, rect_y + shadow_offset, rect_width, rect_height)
    pygame.draw.rect(screen, GREEN, (360, 260, 100, 50 ))
    pygame.draw.rect(screen, (0, 0, 0), (rect_x, rect_y, rect_width, rect_height))
    pygame.display.update()


while True:
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                rect_y -= 10
            elif event.key == pygame.K_s:
                rect_y += 10
            elif event.key == pygame.K_a:
                rect_x -= 10
            elif event.key == pygame.K_d:
                rect_x += 10
