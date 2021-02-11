from screeninterface import *
from settings import *
from os import path
import random

class Question1(ScreenInterface):
    def __init__(self, game):
        self.game = game
        self.correct_answer = ""


    def question_get(self):
        dir = path.dirname(__file__)
        data_dir = path.join(dir, 'data')
        quiz_database = path.join(data_dir, 'quizdatabase.txt')
        f = open(quiz_database, "r")
        for line in f:
            fields = line.split("|")
        question = fields[0]
        self.correct_answer = fields[1]
        wrong_answer1 = fields[2]
        wrong_answer2 = fields[3]
        wrong_answer3 = fields[4]
        tags = fields[5]
        questions.append(self.correct_answer)
        questions.append(wrong_answer1)
        questions.append(wrong_answer2)
        questions.append(wrong_answer3)

        random.shuffle(questions)


        # pytanie, all_answers[], correct_answer



    def screenRun(self):

        self.game.draw_text('The first question is... ' + fields[0], 32, BLACK, WIDTH / 2, HEIGHT / 4)

        self.game.create_button('A: ' + self.questions[1], self.questions[1], BLACK, RED, 60, 30, WIDTH / 4, HEIGHT / 3)
        self.game.create_button('B: ' + self.questions[2], self.questions[2], BLACK, RED, 60, 30, WIDTH / 1.25, HEIGHT / 3)
        self.game.create_button('C: ' + self.questions[3], self.questions[3], BLACK, RED, 60, 30, WIDTH / 4, HEIGHT / 2)
        self.game.create_button('D: ' + self.questions[4], self.questions[4], BLACK, RED, 60, 30, WIDTH / 1.25, HEIGHT / 2)


        self.game.create_button('Menu', 'menu', BLACK, RED, 100, 50, WIDTH / 2, HEIGHT / 1.5)
        self.game.create_button('BACK', 'back', BLACK, RED, 100, 50, WIDTH / 4, HEIGHT / 1.5)

    def button_function_run(self):
        if self.game.pressed == self.correct_answer:
            self.game.draw_text('CORRECT!', 32, BLACK, WIDTH / 2, HEIGHT / 1.75)
        if self.game.pressed != 'EMPTY' and self.game.pressed != self.questions[0]:
            self.game.draw_text('wrong!', 32, BLACK, WIDTH / 2, HEIGHT / 1.75)
        #if self.game.pressed == 'b':
        #    self.game.draw_text('MAYBE NEXT TIME', 32, BLACK, WIDTH / 2, HEIGHT / 1.75)
        #if self.game.pressed == 'c':
        #    self.game.draw_text('TRY AGAIN!', 32, BLACK, WIDTH / 2, HEIGHT / 1.75)
        #if self.game.pressed == 'd':
        #    self.game.draw_text('WRONG', 32, BLACK, WIDTH / 2, HEIGHT / 1.75)
        if self.game.pressed == 'menu':
            self.game.current_screen = self.game.menu_1
        if self.game.pressed == 'back':
            self.game.current_screen = self.game.start_screen
