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
        self.all_read_questions = []
        self.all_unread_questions_capital = []
        self.all_unread_questions_dict = {'capital':[],
                                          'attractions': [],
                                            'food': []}
        self.question_count = 0
        self.current_category = ""

    def new_question(self):
        dir = path.dirname(__file__)
        data_dir = path.join(dir, 'data')
        quiz_database = path.join(data_dir, 'quizdatabase.txt')
        f = open(quiz_database, "r")
        next(f)
        for line in f:
            fields = line.split("|")
            self.all_unread_questions_dict[str(fields[5])].append(fields)
        for key in self.all_unread_questions_dict:
            random.shuffle(self.all_unread_questions_dict[key])

    def question_get_from_category(self):
        if self.all_unread_questions_dict[self.current_category] == []:
            self.new_question()
        if self.all_unread_questions_dict[self.current_category] == []:
            print("Error: " + self.current.category + " category not found in database")
        fields = self.all_unread_questions_dict[self.current_category][0]
        self.all_read_questions.append(fields)
        self.all_unread_questions_dict[self.current_category].remove(fields)
        return fields

    def question_get(self):
        fields = self.question_get_from_category()
        question = fields[0]
        self.correct_answer = fields[1]

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

        self.game.draw_text('The question is... ' + self.current_question[0], 35, TEXT_COLOR, WIDTH / 2, HEIGHT / 4)
        self.game.create_button('A: ' + self.current_question[1][0], self.current_question[1][0], WHITE, DARK_PURPLE, 150, 40, WIDTH / 4, HEIGHT / 2.75)
        self.game.create_button('B: ' + self.current_question[1][1], self.current_question[1][1], WHITE, DARK_PURPLE, 150, 40, WIDTH / 1.25, HEIGHT / 2.75)
        self.game.create_button('C: ' + self.current_question[1][2], self.current_question[1][2], WHITE, DARK_PURPLE, 150, 40, WIDTH / 4, HEIGHT / 1.75)
        self.game.create_button('D: ' + self.current_question[1][3], self.current_question[1][3], WHITE, DARK_PURPLE, 150, 40, WIDTH / 1.25, HEIGHT / 1.75)

        self.game.draw_text('The current category is: ' + self.current_category, 25, TEXT_COLOR, WIDTH / 2, HEIGHT * 0.15)

        self.game.create_button('MENU', 'menu', WHITE, DARK_GREEN, 150, 40, WIDTH / 3, HEIGHT / 1.15)
        self.game.create_button('BACK', 'back', WHITE, DARK_GREEN, 150, 40, WIDTH / 1.5, HEIGHT / 1.15)

        self.game.draw_text(str(int(self.game.score)), 20, TEXT_COLOR, WIDTH / 2, 10)

    def button_function_run(self):
        if self.game.pressed == self.current_question[2]:
            self.game.add_score(POINTS)
            self.screen_question_end_show_correct()
        if self.game.pressed in self.current_question[1] and self.game.pressed != self.current_question[2]:
            self.screen_question_end_show_wrong()
        if self.game.pressed == 'menu':
            self.game.current_screen = self.game.menu_screen
        if self.game.pressed == 'back':
            self.game.current_screen = self.game.start_screen

    def screen_question_end_show_correct(self):
        self.game.screen.fill(BACKGROUND_COLOR)
        self.game.draw_text('CORRECT!', 35, TEXT_COLOR, WIDTH / 2, HEIGHT / 3.5)
        self.game.draw_text('+ ' + str(POINTS), 32, TEXT_COLOR ,WIDTH / 2, HEIGHT * 0.1)
        self.game.screen_flip()
        time.sleep(1)
        self.next_question()

    def screen_question_end_show_wrong(self):
        self.game.screen.fill(BACKGROUND_COLOR)
        self.game.draw_text('WRONG', 35, TEXT_COLOR, WIDTH / 2, HEIGHT / 3.5)
        self.game.draw_text('The correct answer was ' + self.correct_answer, 25, TEXT_COLOR, WIDTH / 2, HEIGHT / 2.5)
        self.game.screen_flip()
        time.sleep(1.5)
        self.next_question()

    def next_question(self):
        #to keep track of questions
        self.current_question = self.question_get()
        self.question_count += 1
        if self.question_count == QUESTION_COUNT:
            self.game.current_screen = self.game.game_over_screen
            self.question_count = 0
            self.game.final_score()
