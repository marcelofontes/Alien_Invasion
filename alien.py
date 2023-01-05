import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
#classe que representa um unico alienígena da frota
    def __init__(self, ai_settings, screen):
        #inicializa o alienigena e define sua posição
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #carrega a imagem do alienigena e define seu atributo rect 
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #inicia cada novo alienigena proximo a parte superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #armazena a posicao exata do alienigena
        self.x = float(self.rect.x)

    
    def blitme(self):
        #desenha o alienigena em sua posicao atual
        self.screen.blit(self.image, self.rect)
   

    def check_edges(self):
        #devolve True se o alienigena estiver na borda da tela
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True    
        else:
            return False

        
    def update(self):
            #move o alienigena para a direita ou para a esquerda
            self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
            self.rect.x = self.x
        