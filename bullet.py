import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #classe que administra projéteis disparados pela espaçonave

    def __init__(self, ai_settings, screen, ship):
        #cria um objeto para o projetil na posição atual
        super(Bullet,self).__init__()
        self.screen = screen

    #cria um retangulo para o projetil em (0,0) e, em seguinda, defina a posição
    #correta
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

    #armazena a posição do projetil como um valor decimal
        self.y = float(self.rect.y)
        self.color=ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        #atualiza a posição do projetil
        self.y -= self.speed_factor
        #atualiza a posição de rect
        self.rect.y = self.y
    
    def draw_bullet(self):
        #desenha o projetil na tela
        pygame.draw.rect(self.screen, self.color, self.rect)


