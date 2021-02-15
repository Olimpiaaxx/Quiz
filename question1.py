from screeninterface import *
from settings import *
from os import path
import random

class Question1(ScreenInterface):
    def __init__(self, game):
        self.game = game
        self.current_question = []
        self.got_question = False
        self.all_unread_questions = []
        self.all_read_questions = []
        # do 2 new lists, one with not read questions and one with read questions

        # create new function here which will put all questions into new list

    def new_question(self):
        dir = path.dirname(__file__)
        data_dir = path.join(dir, 'data')
        quiz_database = path.join(data_dir, 'quizdatabase.txt')
        f = open(quiz_database, "r")
        next(f)
        for line in f:
            fields = line.split("|")
            self.all_unread_questions.append(fields)
            random.shuffle(self.all_unread_questions)
        #    for item in f:
        #        skip = True
        #        if skip:
        #            skip = False
        #            continue

        # change below function to read record from the new list and put the previous into read questions list
    def question_get(self):
        if self.all_unread_questions == []:
            self.new_question()

        #print(self.all_unread_questions)
        fields = self.all_unread_questions[0]
        self.all_read_questions.append(fields)
        question = fields[0]
        correct_answer = fields[1]
        #tags = fields[5]
        answers = []
        answers.append(fields[1])
        answers.append(fields[2])
        answers.append(fields[3])
        answers.append(fields[4])

        random.shuffle(answers)
        return [question, answers, correct_answer]


    def screenRun(self):
        if not self.got_question:
            self.current_question = self.question_get()
            self.got_question = True


        self.game.draw_text('The first question is... ' + self.current_question[0], 32, BLACK, WIDTH / 2, HEIGHT / 4)

        self.game.create_button('A: ' + self.current_question[1][0], self.current_question[1][0], BLACK, RED, 60, 30, WIDTH / 4, HEIGHT / 3)
        self.game.create_button('B: ' + self.current_question[1][1], self.current_question[1][1], BLACK, RED, 60, 30, WIDTH / 1.25, HEIGHT / 3)
        self.game.create_button('C: ' + self.current_question[1][2], self.current_question[1][2], BLACK, RED, 60, 30, WIDTH / 4, HEIGHT / 2)
        self.game.create_button('D: ' + self.current_question[1][3], self.current_question[1][3], BLACK, RED, 60, 30, WIDTH / 1.25, HEIGHT / 2)


        self.game.create_button('Menu', 'menu', BLACK, RED, 100, 50, WIDTH / 2, HEIGHT / 1.5)
        self.game.create_button('BACK', 'back', BLACK, RED, 100, 50, WIDTH / 4, HEIGHT / 1.5)

    def button_function_run(self):
        if self.game.pressed == self.current_question[2]:
            self.game.draw_text('CORRECT!', 32, BLACK, WIDTH / 2, HEIGHT / 1.75)
        if self.game.pressed in self.current_question[1] and self.game.pressed != self.current_question[2]:
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
