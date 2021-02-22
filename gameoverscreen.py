from screeninterface import *
from settings import *

class GameOverScreen(ScreenInterface):
    def __init__(self, game):
        self.game = game

    def screen_run(self):
        self.game.draw_text('You have answered all the questions', 32, BLACK, WIDTH / 2, HEIGHT / 4)
        self.game.draw_text('Your points: '+ str(self.game.score), 15, BLACK, WIDTH / 2, HEIGHT / 2.75)
        self.game.draw_text('Your total points: '+ str(self.game.total_score), 15, BLACK, WIDTH / 2, HEIGHT / 2)
        self.game.create_button('Play Again', 'playagain', YELLOW, GREEN, 120, 80, WIDTH / 2, HEIGHT / 1.25)

    def button_function_run(self):
        if self.game.pressed == 'playagain':
            self.game.current_screen = self.game.start_screen
