from pygame.font import SysFont
from settings import WHITE

def display_score(screen,score):
    font_style = SysFont('Arial', size = 25)
    message = font_style.render(f'Очки: {score}', True, WHITE)
    screen.blit(message, [10,10])