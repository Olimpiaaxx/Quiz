import pygame
import random
from screeninterface import *
from quizfile import *
from os import path
from sys import exit
from settings import *
from Menu1 import *
from startscreen import *
from question1 import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.font_name = pygame.font.match_font(FONT_NAME)
        pygame.display.set_caption("Welcome to the QUIZ!")
        self.running = False
        self.pressed = 'EMPTY'
        self.all_sprites = pygame.sprite.Group()
        self.all_buttons = []
        self.menu_1 = Menu1(self)
        self.start_screen = StartScreen(self)
        self.question_1 = Question1(self)
        self.current_screen = self.menu_1 # tells you what screen the program is on

    def reset_buttons(self):
        self.pressed = 'EMPTY'

    def draw_text(self, text, size, color, x, y):
        self.font_name = pygame.font.match_font("arial")
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def create_button(self, text, buttonValue, t_color, b_color, w, h, x, y):
        button = Button(self, text, buttonValue, t_color, b_color, w, h, x, y)
        self.all_buttons.append(button)

    def show_start_screen(self):
        self.running = True
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill(WHITE)
        self.current_screen.screenRun()
        self.current_screen.button_function_run()
        self.reset_buttons()

        if pygame.mouse.get_pressed()[0]:
            for button in self.all_buttons:
                if button.check_if_collided(pygame.mouse.get_pos()):
                    self.pressed = button.buttonValue


        pygame.display.flip()

class Button(pygame.sprite.Sprite):
    def __init__(self, game, text, buttonValue, t_color, b_color, w, h, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.text = text
        self.buttonValue = buttonValue
        self.t_color = t_color
        self.b_color = b_color
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.draw_on_screen()

    def check_if_collided(self, pos):
        a = pos[0] > self.x - (self.w / 2) and pos[0] < self.x + (self.w / 2)
        b = pos[1] > self.y + (self.h / 2 * 0.6) - (self.h / 2) and pos[1] < self.y + (self.h / 2 * 0.6) + (self.h / 2)
        return a and b


    def draw_on_screen(self):
        # Main functionality
        # Create box here
        pygame.draw.rect(self.game.screen, self.b_color, (self.x - (self.w / 2), self.y - (self.h/2 * 0.4), self.w, self.h))
        # Last
        self.show_text()

    def show_text(self):
        self.game.draw_text(self.text, int(self.h/2), self.t_color, self.x, self.y)

    def press(self):
        return self.buttonValue


g = Game()
g.show_start_screen()
while g.running:
    #g.new()
    g.show_start_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            g.running = False






## TODO:
#find how to end the screen
#pygame.display.quit()
pygame.quit()
exit()
