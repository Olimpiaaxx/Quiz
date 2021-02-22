from screeninterface import *
from settings import *

class MenuScreen(ScreenInterface):
    def __init__(self, game):
        self.game = game

    def screen_run(self):
        self.game.draw_text('Its time to play a game!', 32, BLACK, WIDTH / 2, HEIGHT / 4)
        self.game.draw_text('by Olimpia', 15, BLACK, WIDTH / 2, HEIGHT / 2.75)
        self.game.create_button('Start', 'start', YELLOW, GREEN, 120, 80, WIDTH / 2, HEIGHT / 1.75)

    def button_function_run(self):
        if self.game.pressed == 'start':
            self.game.current_screen = self.game.start_screen
