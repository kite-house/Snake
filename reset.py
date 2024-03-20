from menu import menu

def reset(screen ,snake_length):
    menu.loose_menu(snake_length).mainloop(screen)
    snake_length = 1
    return snake_length
    