class Settings():
    """Uma classe para armazenar todas as configurações do jogo"""

    def __init__(self):
        #inicializa as configurações do jogo

        #configurações da espaçonave
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        

        #configurações dos projéteis
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3

        #configurações dos alienigenas
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        #a taxa com que a velocidade do jogo aumenta
        self.speedup_scale = 1.1
        # taxa com que os pontos para cada alien aumentam
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        #inicializa as configurações que mudam no decorrer do jogo
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        #pontuação
        self.alien_points = 50


    def increase_speed(self):
        #aumenta as configurações de velocida
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points *= int(self.alien_points * self.score_scale)
        print(self.alien_points)


