from modules.menu import Menu

def reset(screen):
    Menu('Вы проиграли!', 'Продолжить игру').launch(screen)
    return 1
    