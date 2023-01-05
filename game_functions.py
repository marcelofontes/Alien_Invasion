import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    #responde a eventos de pressionamento de teclas e de mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()       
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button,ship,aliens, bullets,  mouse_x, mouse_y) 
           

def check_play_button( ai_settings, screen, stats, sb, play_button,ship, aliens, bullets,  mouse_x, mouse_y):
    
    #inicia um novo jogo quando o jogador clicar em play
    button_clicked  = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #reinicia as configurações do jogo 
        ai_settings.initialize_dynamic_settings()
        #oculta o cursor do mouse
        pygame.mouse.set_visible(False)
        #reinicia os dados estatisticos do jogo
        stats.reset_stats()
        stats.game_active = True
        #reinicia imagens do painel de pontuação
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        #esvazia a lista de alienigenas e de projeteis
        aliens.empty()
        bullets.empty()
        #cria uma nova frota e centraliza a nave
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()



def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # responde a pressionamentos de tecla
   
    if event.key ==pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #cria um novo projetil e o adiciona ao grupo de projeteis 
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key ==pygame.K_RIGHT:
        ship.moving_right = False
        #move a nave para a esquerda
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    #atualiza as imagens na tela e alterna para a nova tela

    #redesenha a tela a cada passagem pelo laço
    screen.fill(ai_settings.bg_color)

    
    #redesenha todos os projeteis atras da espaçonave e dos alienigenas
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)


    # desenha a informação sobre pontuação
    sb.show_score()

    #desenha o botao play se o jogo estiver inativo 
    if not stats.game_active:
        play_button.draw_button()

    #deia a tela mais recente visível
    pygame.display.flip()
   

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    #atualiza a posicao dos projeteis e se livra dos projeteis antigos
    #atualiza a posição dos projeteis
    bullets.update()

    #livra-se dos projeteis que desaparecem
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)
    
    
def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    #responde a colisores entre projeteis e alienígenas
    # remove alien e bullet que colidiram  
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():          
            stats.score += ai_settings.alien_points*len(aliens)
            sb.prep_score()
    check_high_score(stats, sb)

    #se a frota for destruida, inicia um novo nivel
    if len(aliens) == 0:
        #destroi os projeteis existentes e cria uma nova frota de aliens
        bullets.empty()
        ai_settings.increase_speed()
        #aumenta o nivel
        stats.level += 1
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    #dispara um projetil se o limite ainda nao foi alcançado
    #cria um novo projetil e o adiciona ao grupo de projeteis
         if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)


def create_fleet(ai_settings, screen, ship, aliens):
    #cria uma frota completa de alienigenas
    #cria um alienigena e calcula o numero de alienigenas em uma linha
    #o espaçamento entre os alienigenas e igual a largura de um alienigena
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    #cria a frota de alienigenas
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    #determina o numero de alienigenas que cabem em uma linha
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x / (2*alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    #cria um alienigena e o posiciona na linha 
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    #determina o numero de linhas com alienigenas que cabem na tela
    available_space_y = (ai_settings.screen_height - 3*alien_height - ship_height)
    number_rows = int(available_space_y / (2*alien_height))
    return number_rows


def check_fleet_edges(ai_settings, aliens):
    #responde apropriadamente se algum alienigena alcancou uma borda
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    #faz toda a frota descer e muda sua direção
    for alien in aliens.sprites():    
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
       

def update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets):
    #verifica se a frota está em uma das bordas e entao atualza as posições de todos os 
    #alienigenas da frota
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    #verifica se houve colisao entre nave e alin
    if pygame.sprite.spritecollideany(ship, aliens):
       ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)

    #verifica se algum alien atingiou a parte inferior da tela
    check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets)


def ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets):

    # responde quando a nave é atingida por um alien
    #decrementa ships_left
    if stats.ships_left > 0:
        stats.ships_left-=1

        #atualiza painel de pontuacoes
        sb.prep_ships()

        #esvazia a lista de aliens e projeteis
        aliens.empty()
        bullets.empty()

        #cria uma nova frota e centraliza a nave
        create_fleet(ai_settings, screen,ship, aliens )
        ship.center_ship()

        #faz a uma pausa
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets):
    #verifica se algum alien alcançou a parte inferior da tela
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
            break

def check_high_score(stats,sb):
    #verifica se há uma nova pontuação máxima
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()