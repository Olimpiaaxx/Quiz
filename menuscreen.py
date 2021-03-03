from screeninterface import *
from settings import *

class MenuScreen(ScreenInterface):
    def __init__(self, game):
        self.game = game
        self.game.load_image()

    def screen_run(self):
        self.game.screen.blit(self.game.menu_image, self.game.menu_image_rect)
        self.game.draw_text('Time to test your knowledge', 40, TEXT_COLOR, WIDTH / 2, HEIGHT / 4)
        self.game.draw_text('Created by Olimpia', 20, TEXT_COLOR, WIDTH / 2, HEIGHT / 2.75)
        self.game.create_button('START', 'start', WHITE, DARK_GREEN, 150, 40, WIDTH / 2, HEIGHT / 2)


    def button_function_run(self):
        if self.game.pressed == 'start':
            self.game.current_screen = self.game.start_screen
