from screeninterface import *
from settings import *
from os import path
import random
import time
import pyodbc

class QuestionScreen(ScreenInterface):
    def __init__(self, game):
        self.game = game
        self.current_question = []
        self.got_question = False
        self.all_read_questions = []
        self.all_unread_questions_dict = {'capital':[],
                                          'attractions': [],
                                          'food': [],
                                          'nature': []}
        self.question_count = 0
        self.current_category = ""
        self.game.load_image()

    #Access questions from databse intp a shuffled dictionary
    def new_question(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                                'Server=LAPTOP-5818FKV9\SQLEXPRESS;'
                                'Database=QuizDB;'
                                'Trusted_Connection=Yes;')

        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Quiz')

        # nowalistazczyms = nowafunkcja('SELECT * FROM Quiz')


        for row in cursor:
            fields = [elem for elem in row]
            #fields = row.split(',')
            fields.remove(fields[0])

            self.all_unread_questions_dict[str(fields[5])].append(fields)

        for key in self.all_unread_questions_dict:
            random.shuffle(self.all_unread_questions_dict[key])

    #Takes questions based on the chosen category
    def question_get_from_category(self):
        if self.all_unread_questions_dict[self.current_category] == []:
            self.new_question()
            #to check if database is empty
        if self.all_unread_questions_dict[self.current_category] == []:
            print("Error: " + self.current.category + " category not found in database")

        fields = self.all_unread_questions_dict[self.current_category][0]
        self.all_unread_questions_dict[self.current_category].remove(fields)
        return fields

    #Creates questions
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

    #Main funtion
    def screen_run(self):
        if not self.got_question:
            self.current_question = self.question_get()
            self.got_question = True

        self.game.draw_text('The question is... ' + self.current_question[0], 35, TEXT_COLOR, WIDTH / 2, HEIGHT / 4)
        self.game.create_button('A: ' + self.current_question[1][0], self.current_question[1][0], WHITE, DARK_PURPLE, 150, 40, WIDTH / 3, HEIGHT / 2.75)
        self.game.create_button('B: ' + self.current_question[1][1], self.current_question[1][1], WHITE, DARK_PURPLE, 150, 40, WIDTH / 1.5, HEIGHT / 2.75)
        self.game.create_button('C: ' + self.current_question[1][2], self.current_question[1][2], WHITE, DARK_PURPLE, 150, 40, WIDTH / 3, HEIGHT / 1.75)
        self.game.create_button('D: ' + self.current_question[1][3], self.current_question[1][3], WHITE, DARK_PURPLE, 150, 40, WIDTH / 1.5, HEIGHT / 1.75)

        self.game.draw_text('The current category is: ' + self.current_category, 25, TEXT_COLOR, WIDTH / 2, HEIGHT * 0.15)

        self.game.create_button('MENU', 'menu', WHITE, DARK_GREEN, 150, 40, WIDTH / 3.75, HEIGHT / 1.15)
        self.game.create_button('BACK', 'back', WHITE, DARK_GREEN, 150, 40, WIDTH / 1.35, HEIGHT / 1.15)

        self.game.draw_text(str(int(self.game.score)), 20, TEXT_COLOR, WIDTH / 2, 10)

    def button_function_run(self):
        if self.game.pressed == self.current_question[2]:
            self.game.total_questions_answered_correct += 1
            self.game.add_score(POINTS)
            self.screen_question_end_show_correct()
        if self.game.pressed in self.current_question[1] and self.game.pressed != self.current_question[2]:
            self.game.total_questions_answered_wrong += 1
            self.screen_question_end_show_wrong()
        if self.game.pressed == 'menu':
            self.game.current_screen = self.game.menu_screen
        if self.game.pressed == 'back':
            self.game.current_screen = self.game.start_screen

    def screen_question_end_show_correct(self):
        self.game.screen.fill(BACKGROUND_COLOR)
        self.game.screen.blit(self.game.correct_answer_image, self.game.correct_answer_image_rect)
        self.game.draw_text('CORRECT!', 35, TEXT_COLOR, WIDTH / 2, HEIGHT / 3.5)
        self.game.draw_text('+ ' + str(POINTS), 32, TEXT_COLOR ,WIDTH / 2, HEIGHT * 0.1)
        self.game.screen_flip()
        time.sleep(1)
        self.next_question()

    def screen_question_end_show_wrong(self):
        self.game.screen.fill(BACKGROUND_COLOR)
        self.game.screen.blit(self.game.wrong_answer_image, self.game.wrong_answer_image_rect)
        self.game.draw_text('WRONG', 35, TEXT_COLOR, WIDTH / 2, HEIGHT / 3.5)
        self.game.draw_text('The correct answer was ' + self.correct_answer, 25, TEXT_COLOR, WIDTH / 2, HEIGHT * 0.1)
        self.game.screen_flip()
        time.sleep(1.5)
        self.next_question()

    def next_question(self):
        #to keep track of questions
        self.got_question = False
        self.question_count += 1
        if self.question_count == QUESTION_COUNT:
            self.game.current_screen = self.game.game_over_screen
            self.question_count = 0
            self.game.final_score()
