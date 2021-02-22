from screeninterface import *
from settings import *
from os import path
import random
import time

class QuestionScreen(ScreenInterface):
    def __init__(self, game):
        self.game = game
        self.current_question = []
        self.got_question = False
        self.all_unread_questions = []
        self.all_read_questions = []

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

    def question_get(self):
        if self.all_unread_questions == []:
            self.new_question()
        #print(self.all_unread_questions)
        fields = self.all_unread_questions[0]
        self.all_read_questions.append(fields)
        self.all_unread_questions.remove(fields)
        question = fields[0]
        self.correct_answer = fields[1]
        #tags = fields[5]
        answers = []
        answers.append(fields[1])
        answers.append(fields[2])
        answers.append(fields[3])
        answers.append(fields[4])

        random.shuffle(answers)
        return [question, answers, self.correct_answer]

    def screen_run(self):
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

        self.game.draw_text(str(int(self.game.score)), 18, RED, WIDTH / 2, 10)

    def button_function_run(self):
        if self.game.pressed == self.current_question[2]:
            self.game.add_score(POINTS)
            self.screen_question_end_show_correct()
        if self.game.pressed in self.current_question[1] and self.game.pressed != self.current_question[2]:
            self.screen_question_end_show_wrong()
        if self.game.pressed == 'menu':
            self.game.current_screen = self.game.menu_1
        if self.game.pressed == 'back':
            self.game.current_screen = self.game.start_screen

    def screen_question_end_show_correct(self):
        self.game.screen.fill(BLACK)
        self.game.draw_text('CORRECT!', 32, WHITE, WIDTH / 2, HEIGHT / 1.75)
        self.game.draw_text('+ ' + str(POINTS), 32, WHITE,WIDTH/2, HEIGHT * 0.1)
        self.game.screen_flip()
        time.sleep(1)
        self.next_question()

    def screen_question_end_show_wrong(self):
        self.game.screen.fill(BLACK)
        self.game.draw_text('WRONG', 32, WHITE, WIDTH / 2, HEIGHT / 1.75)
        self.game.draw_text('The correct answer was ' + self.correct_answer, 25, WHITE, WIDTH / 2, HEIGHT / 1.25)
        self.game.screen_flip()
        time.sleep(2)
        self.next_question()

    def next_question(self):
        #to keep track of questions
        self.current_question = self.question_get()
