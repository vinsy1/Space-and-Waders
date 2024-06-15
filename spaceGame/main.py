import pygame
import sys
from button import ImageButton
import controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores

pygame.init()

WIDTH, HEIGHT = 700, 800
MAX_FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Меню")
bg_color = (0, 0, 0)
clock = pygame.time.Clock()

def main_menu():
    start_button = ImageButton(WIDTH/2-(252/2), 150, 252, 114, "Новая игра", "image/butBlue.png")
    settings_button = ImageButton(WIDTH/2-(252/2), 250, 252, 114, "Настройки", "image/butPurple.png")
    exit_button = ImageButton(WIDTH/2-(252/2), 350, 252, 114, "Выйти", "image/butPink.png")

    running = True
    while running:
        screen.fill((0, 0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("Space and Waders", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH/2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == start_button:
                print("Кнопка 'Старт' была нажата!")
                fade()
                new_game()

            if event.type == pygame.USEREVENT and event.button == settings_button:
                print("Кнопка 'Настройки' была нажата!")
                fade()
                settigs_menu()

            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
                pygame.quit()
                sys.exit()

            for btn in [start_button, settings_button, exit_button]:
                btn.handle_event(event)

        for btn in [start_button, settings_button, exit_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

def settigs_menu():
    audio_button = ImageButton(WIDTH/2-(252/2), 150, 252, 114, "Аудио", "image/butBlue.png")
    video_button = ImageButton(WIDTH/2-(252/2), 250, 252, 114, "Видео", "image/butPurple.png")
    back_button = ImageButton(WIDTH/2-(252/2), 350, 252, 114, "Назад", "image/butPink.png")

    running = True
    while running:
        screen.fill((0, 0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("НАСТРОЙКИ", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH/2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    fade()
                    running = False

            if event.type == pygame.USEREVENT and event.button == back_button:
                fade()
                running = False
            
            for btn in [audio_button, video_button, back_button]:
                btn.handle_event(event)

        for btn in [audio_button, video_button, back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen)

        pygame.display.flip()

def new_game():

    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Space and Waders")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, inos, bullets) 
            controls.update_bullets(screen, stats, sc, inos, bullets)
            controls.update_inos(stats, screen, sc, gun, inos, bullets)      
   
pygame.display.flip()

def fade():
    running = True
    fade_alpha = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        fade_surface = pygame.Surface((WIDTH, HEIGHT))
        fade_surface.fill((0, 0, 0))
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))

        fade_alpha += 5
        if fade_alpha >= 105:
            fade_alpha = 255
            running = False

        pygame.display.flip()
        clock.tick(MAX_FPS)

if __name__ == "__main__":
    main_menu()