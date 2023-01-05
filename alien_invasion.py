import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard



def run_game():

    #inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Ivasion - Papai é Foda!!")

    #cria o botao play
    play_button = Button(ai_settings, screen, "Play")

    #cria uma instancia para armazenar estatisticas do jogo  e creia painel de pontuação
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

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
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)  
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
        #redesenha a tela a cada passagem pelo laço
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
       
       
run_game()

