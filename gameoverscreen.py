from screeninterface import *
from settings import *

class GameOverScreen(ScreenInterface):
    def __init__(self, game):
        self.game = game
        self.game.load_image()

    def screen_run(self):
        self.game.screen.blit(self.game.game_over_image, self.game.game_over_image_rect)
        self.game.draw_text('You have answered all the questions', 35, TEXT_COLOR, WIDTH / 2, HEIGHT / 4.75)
        self.game.draw_text('Your points this round: '+ str(self.game.score), 20, TEXT_COLOR, WIDTH / 3, HEIGHT / 3.25)
        self.game.draw_text('Your total points: '+ str(self.game.total_score), 20, TEXT_COLOR, WIDTH / 3, HEIGHT / 2.8)
        self.game.draw_text('Correct answers so far: '+ str(self.game.total_questions_answered_correct), 20, TEXT_COLOR, WIDTH / 1.5, HEIGHT / 3.25)
        self.game.draw_text('Wrong answers so far: '+ str(self.game.total_questions_answered_wrong), 20, TEXT_COLOR, WIDTH / 1.5, HEIGHT / 2.8)
        self.game.create_button('Play Again', 'playagain', WHITE, DARK_PURPLE, 150, 40, WIDTH / 2, HEIGHT / 2)

    def button_function_run(self):
        if self.game.pressed == 'playagain':
            self.game.current_screen = self.game.start_screen
