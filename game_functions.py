import sys
import pygame

def check_events(ship):
    #responde a eventos de pressionamento de teclas e de mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_RIGHT:
                ship.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key ==pygame.K_RIGHT:
                ship.moving_right = False
                #move a espaçonave para a direita
          

def update_scren(ai_settings, screen, ship):
    #atualiza as imagens na tela e alterna para a nova tela
    #redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    #deia a tela mais recente visível
    pygame.display.flip()

