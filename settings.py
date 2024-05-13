import pygame

# PARAM
WIDTH, HEIGHT = 600, 400
SIZE = 25
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
eat = pygame.mixer.Sound("particles/sounds/eat.mp3")
game_over = pygame.mixer.Sound("particles/sounds/gameover.mp3")
bg = pygame.mixer.Sound("particles/sounds/bg.mp3")

food_img = pygame.transform.scale(pygame.image.load("particles/img/food.png"), (SIZE,SIZE))

head_snake = [
    pygame.transform.scale(pygame.image.load("particles/img/headB.png"), (SIZE,SIZE)),
    pygame.transform.scale(pygame.image.load("particles/img/headL.png"), (SIZE,SIZE)),
    pygame.transform.scale(pygame.image.load("particles/img/headR.png"), (SIZE,SIZE)),
    pygame.transform.scale(pygame.image.load("particles/img/headT.png"), (SIZE,SIZE))
]
body_snake = pygame.transform.scale(pygame.image.load("particles/img/body.png"), (SIZE,SIZE))

tail_snake = [
    pygame.transform.scale(pygame.image.load("particles/img/TailD.png"), (SIZE,SIZE)),
    pygame.transform.scale(pygame.image.load("particles/img/TailL.png"), (SIZE,SIZE)),
    pygame.transform.scale(pygame.image.load("particles/img/TailR.png"), (SIZE,SIZE)),
    pygame.transform.scale(pygame.image.load("particles/img/TailU.png"), (SIZE,SIZE))
]
