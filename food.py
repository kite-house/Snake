import random
from settings import *

class Food():
    def __init__(self, HEIGHT, WIDTH):
        self.y = random.randrange(10, HEIGHT - 10, 5)
        self.x = random.randrange(10, WIDTH - 10, 5)
