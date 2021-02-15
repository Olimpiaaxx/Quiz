from screeninterface import *
from settings import *

class StartScreen(ScreenInterface):
    def __init__(self, game):
        self.game = game

    def screenRun(self):
        self.game.draw_text('This is your start screen', 32, BLACK, WIDTH / 2, HEIGHT / 4)

        self.game.create_button('Menu', 'menu', BLACK, RED, 100, 50, WIDTH / 2, HEIGHT / 3)
        self.game.create_button('Start Game', 'startGame', RED, BLUE, 120, 50, WIDTH / 4, HEIGHT / 1.7)

    def button_function_run(self):
        if self.game.pressed == 'menu':
            self.game.current_screen = self.game.menu_1
        if self.game.pressed == 'startGame':
            self.game.current_screen = self.game.question_1
