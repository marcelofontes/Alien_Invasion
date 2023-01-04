import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf



def run_game():

    #inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Ivasion - Papai é Foda!!")

    #cria uma espaçonave
    ship = Ship(ai_settings, screen)
    #cria um grupo no qual sao armazenados os projeteis
    bullets = Group()
    #cria uma frota de aliens
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

       #define a cor de fundo
    bg_color = (ai_settings.bg_color)

    #inicia o laço principal do jogo
    while True:
    #observa eventos de teclado e de mouse
        gf.check_events(ai_settings, screen, ship, bullets)  
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        
        #redesenha a tela a cada passagem pelo laço
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
       
       
run_game()

