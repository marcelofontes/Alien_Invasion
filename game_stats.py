
class GameStats():

    def __init__(self, ai_settings):
        #inicializa dados estatítticos
        self.ai_settings = ai_settings

        #inicia o jogo em estado inativo
        self.game_active = False
        self.reset_stats()
        #a pontuação máxima jamais deverá ser reiniciada
        self.high_score = 0

        #prepara as images das pontuacoes iniciais 
       

    def reset_stats(self):
        #incializa os dados estatisticos que podem mudar o jogo
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    
    


