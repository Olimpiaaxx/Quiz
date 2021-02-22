from screeninterface import *
from settings import *

class StartScreen(ScreenInterface):
    def __init__(self, game):
        self.game = game

    def screen_run(self):
        self.game.reset_score()
        self.game.draw_text('Are you ready?', 32, BLACK, WIDTH / 2, HEIGHT / 4)
        self.game.create_button('Menu', 'menu', BLACK, RED, 120, 50, WIDTH / 4, HEIGHT / 1.25)
        self.game.create_button('Start Game', 'startGame', YELLOW, GREEN, 100, 80, WIDTH / 2, HEIGHT / 3)

    def button_function_run(self):
        if self.game.pressed == 'menu':
            self.game.current_screen = self.game.menu_screen
        if self.game.pressed == 'startGame':
            self.game.current_screen = self.game.question_screen
