import tkinter as tk
from screeninterface import *
from settings import *

class LoginScreen:
    def __init__(self, game):
        self.game = game


    def login(self):
        login_window = tk.Label(text='Please log in')
        login_window.pack()
        window.mainloop()




    def register(self):
        pass

    def screen_run(self):
        self.game.draw_text('Would you like to log in?', 32, TEXT_COLOR, WIDTH / 2, HEIGHT / 4)
        self.game.draw_text('Or register if this is your first time here ', 32, TEXT_COLOR, WIDTH / 2, HEIGHT / 3)

        self.game.create_button('Login', 'login', WHITE, DARK_PURPLE, 150, 40, WIDTH / 6, HEIGHT / 2.2)

        self.game.create_button('Register', 'register', WHITE, DARK_PURPLE, 150, 40, WIDTH / 1.2, HEIGHT / 2.2)

        self.game.create_button('MENU', 'menu', WHITE, DARK_GREEN, 150, 40, WIDTH / 2, HEIGHT / 1.25)

    def button_function_run(self):
        if self.game.pressed == 'menu':
            self.game.current_screen = self.game.menu_screen

        if self.game.pressed == 'login':


            self.game.current_screen = self.game.start_screen

        if self.game.pressed == 'register':



            self.game.current_screen = self.game.start_screen
