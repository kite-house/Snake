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
food_img = pygame.transform.scale(pygame.image.load("particles/img/food.png"), (SIZE,SIZE))
eat = pygame.mixer.Sound("particles/sounds/eat.mp3")
game_over = pygame.mixer.Sound("particles/sounds/gameover.mp3")
bg = pygame.mixer.Sound("particles/sounds/bg.mp3")
head_snake_img = pygame.transform.scale(pygame.image.load("particles/img/head_snake.png"), (SIZE,SIZE))
tail_snake_img = pygame.transform.scale(pygame.image.load("particles/img/tail_snake.png"), (SIZE,SIZE))
body_snake_img = pygame.transform.scale(pygame.image.load("particles/img/body_snake.png"), (SIZE,SIZE))