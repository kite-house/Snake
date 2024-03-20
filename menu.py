import pygame_menu
from settings import WIDTH, HEIGHT

class Menu:
    def main_menu(self):
        self.mainmenu = pygame_menu.Menu('Начинаем?' , WIDTH, HEIGHT, theme= pygame_menu.themes.THEME_DARK)
        self.mainmenu.add.button('Играть', self.mainmenu.disable)
        self.mainmenu.add.button('Выход', quit)
        return self.mainmenu
    
    def loose_menu(self, balls):
        self.looseMenu = pygame_menu.Menu(f'Вы проиграли! Очки: {balls - 1}' , WIDTH, HEIGHT, theme= pygame_menu.themes.THEME_DARK)
        self.looseMenu.add.button('Играть', self.looseMenu.disable)
        self.looseMenu.add.button('Выход', quit)
        return self.looseMenu

menu = Menu()