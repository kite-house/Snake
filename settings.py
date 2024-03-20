import pygame

# PARAM
WIDTH, HEIGHT = 600, 400
SIZE = 20
FPS = 60

# COLOR
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#Control 
vector = None

#Sprites
pygame.init()
food_img = pygame.transform.scale(pygame.image.load("img/food.png"), (SIZE,SIZE))
eat = pygame.mixer.Sound("sounds\eat.mp3")
game_over = pygame.mixer.Sound("sounds\gameover.mp3")
bg = pygame.mixer.Sound("sounds/bg.mp3")
head_snake_img = pygame.transform.scale(pygame.image.load("img/head_snake.png"), (SIZE,SIZE))
tail_snake_img = pygame.transform.scale(pygame.image.load("img/tail_snake.png"), (SIZE,SIZE))
body_snake_img = pygame.transform.scale(pygame.image.load("img/body_snake.png"), (SIZE,SIZE))