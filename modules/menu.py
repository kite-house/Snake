import pygame_menu
from settings import WIDTH, HEIGHT

config = {
    'main' : {
        'title' : 'Основное меню',
        'textOneButton' : 'Начать игру',
        'textTwoButton' : 'Выход'
    },
    'pause' : {
        'title' : 'Пауза',
        'textOneButton' : 'Продолжить игру',  
        'textTwoButton' : 'Выход'
    },
    'loose' : {
        'title' : 'Вы проиграли!',
        'textOneButton' : 'Начать заного',
        'textTwoButton' : 'Выход'
    },
}

class Menu:
    def __init__(self, mod):
        self.menu = pygame_menu.Menu(config[mod]['title'], WIDTH, HEIGHT, theme = pygame_menu.themes.THEME_DARK)
        self.menu.add.button(config[mod]['textOneButton'], self.menu.disable)
        self.menu.add.button(config[mod]['textTwoButton'], quit)

    def launch(self, screen):
        self.menu.mainloop(screen)