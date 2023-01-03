import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():

    #inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_with,ai_settings.screen_height))
    pygame.display.set_caption("Alien Ivasion")
    #cria uma espaçonave
    ship = Ship(screen)
    #define a cor de fundo
    bg_color = (ai_settings.bg_color)
    #inicia o laço principal do jogo
    
    while True:
    #observa eventos de teclado e de mouse
        gf.check_events(ship)  
        ship.update()
        #redesenha a tela a cada passagem pelo laço
        gf.update_scren(ai_settings, screen, ship)
       

run_game()

