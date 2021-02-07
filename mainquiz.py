import pygame
import random
from quizfile import *
from os import path


WIDTH = 480
HEIGHT = 600
# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)



class Quiz:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        #pygame.display.set_caption("Welcome to the QUIZ!")
        self.running = False

    def draw_text(self, text, size, color, x, y):
        self.font_name = pygame.font.match_font("arial")
        font = pygame.font.Font(self.font_name, 20)
        text_surface = font.render("QUIZ", True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def show_start_screen(self):
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
            self.screen.fill(BLACK)
            self.draw_text(screen, "Welcome to the QUIZ!", 64, WIDTH / 2, HEIGHT / 4)
            self.draw_text(screen, "by Olimpia", 35, WIDTH / 2, HEIGHT / 2.75)
            self.running = True
            pygame.display.flip()

q = Quiz()
q.show_start_screen()
while q.running:
    #q.new()
    q.show_start_screen()


## TODO:
#find how to end the screen
pygame.quit()
