import random

class Food():
    def __init__(self, HEIGHT, WIDTH):
        self.y = random.randrange(0, HEIGHT, 5)
        self.x = random.randrange(0, WIDTH, 5)