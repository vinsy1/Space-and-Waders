from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes


pygame.init()
surface = pygame.display.set_mode((700, 800))
 
def set_difficulty(value, difficulty):
    print(value)
    print(difficulty)
 
def start_the_game():
    mainmenu._open(loading)
    pygame.time.set_timer(update_loading, 30)
 
# def level_menu():
#     mainmenu._open(level)
 
 
mainmenu = pygame_menu.Menu('Меню', 700, 800, theme=themes.THEME_GREEN)
mainmenu.add.text_input('Ваш Ник: ', default=' ')
mainmenu.add.button('Старт', start_the_game)
# mainmenu.add.button('Levels', level_menu)
mainmenu.add.button('Выход', pygame_menu.events.EXIT)
 
# level = pygame_menu.Menu('Select a Difficulty', 600, 400, theme=themes.THEME_BLUE)
# level.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
 
loading = pygame_menu.Menu('Загрузка игры...', 700, 800, theme=themes.THEME_GREEN)
loading.add.progress_bar("Прогресс", progressbar_id = "1", default=0, width = 200, )
 
arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size = (10, 15))
 
update_loading = pygame.USEREVENT + 0
 
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == update_loading:
            progress = loading.get_widget("1")
            progress.set_value(progress.get_value() + 1)
            if progress.get_value() == 100:
                pygame.time.set_timer(update_loading, 0)
        if event.type == pygame.QUIT:
            exit()
 
    if mainmenu.is_enabled():
        mainmenu.update(events)
        mainmenu.draw(surface)
        if (mainmenu.get_current().get_selected_widget()):
            arrow.draw(surface, mainmenu.get_current().get_selected_widget())
 
    pygame.display.update()