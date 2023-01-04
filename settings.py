class Settings():
    """Uma classe para armazenar todas as configurações do jogo"""

    def __init__(self):
        #inicializa as configurações do jogo

        #configurações da espaçonave
        self.ship_speed_factor = 1.5
        #configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #configurações dos projéteis
        self.bullet_speed_factor = 50
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3

        #configurações dos alienigenas
        self.alien_speed_factor = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
