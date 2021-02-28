from screeninterface import *
from settings import *

class StartScreen(ScreenInterface):
    def __init__(self, game):
        self.game = game

    def screen_run(self):
        self.game.reset_score()
        self.game.draw_text('Are you ready?', 32, TEXT_COLOR, WIDTH / 2, HEIGHT / 4)
        self.game.draw_text('Choose your category: ', 32, TEXT_COLOR, WIDTH / 2, HEIGHT / 3)
        self.game.create_button('Capital', 'capital', WHITE, DARK_PURPLE, 150, 40, WIDTH / 4, HEIGHT / 2.3)
        self.game.create_button('Attractions', 'attractions', WHITE, DARK_PURPLE, 150, 40, WIDTH / 2, HEIGHT / 2.3)
        self.game.create_button('Food', 'food', WHITE, DARK_PURPLE, 150, 40, WIDTH / 1.25, HEIGHT / 2.3)

        self.game.create_button('MENU', 'menu', WHITE, DARK_GREEN, 150, 40, WIDTH / 2, HEIGHT / 1.25)

    def button_function_run(self):
        if self.game.pressed == 'menu':
            self.game.current_screen = self.game.menu_screen
        if self.game.pressed == 'capital':
            self.game.current_screen = self.game.question_screen
            self.game.current_screen.current_category = 'capital'
        if self.game.pressed == 'attractions':
            self.game.current_screen = self.game.question_screen
            self.game.current_screen.current_category = 'attractions'
        if self.game.pressed == 'food':
            self.game.current_screen = self.game.question_screen
            self.game.current_screen.current_category = 'food'
