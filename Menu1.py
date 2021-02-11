from screeninterface import *
from settings import *

class Menu1(ScreenInterface):
    def __init__(self, game):
        self.game = game

    def screenRun(self):
        self.game.draw_text('Welcome to the QUIZ', 32, BLACK, WIDTH / 2, HEIGHT / 4)
        self.game.draw_text('by Olimpia', 15, BLACK, WIDTH / 2, HEIGHT / 2.75)

        self.game.create_button('Start', 'start', YELLOW, GREEN, 80, 40, WIDTH / 2, HEIGHT / 5)
        self.game.create_button('HELLO', 'hello', RED, BLUE, 100, 50, WIDTH / 4, HEIGHT / 2)
        self.game.create_button('Sylan', 'sylan', BLACK, YELLOW, 200, 100, 260, 230)
        self.game.draw_text(self.game.pressed, 40, RED, 200, 400)


    def button_function_run(self):
        if self.game.pressed == 'start':
            self.game.current_screen = self.game.start_screen
        if self.game.pressed == 'hello':
            self.game.draw_text('HELLO SYLAN!', 50, BLACK, WIDTH / 2, HEIGHT / 2.75)
