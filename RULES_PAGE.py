from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from timeit import default_timer as timer
import random
import os
from SPEED_TYPING_TEST import *

os.system("clear")

class Rules_Page:
    def __init__(self, root):
        self.root = root
        self.root.title("TYPING TEST")
        self.root.geometry("1440x880+0+0")

        self.bg_img = ImageTk.PhotoImage(file = "/Users/saniha/Dropbox/My Mac (niha का MacBook Air)/Desktop/NIKSH/IMAGES/BACKGROUNDS/bg_img_7.jpg")
        bg = Label(self.root, image = self.bg_img)
        bg.place(x = 0, y = 120)

        def Exit():
            self.root.destroy()

        def Create_New_Game():
            Exit()
            Start_Game()

        title = Label(self.root, text = "TYPING TEST", font = ("times new roman", 100, "bold"), bg = "yellow", fg = "red", bd = 10, relief = GROOVE)
        title.place(x = 0, y = 0, relwidth = 1)

        my_canvas = Canvas(self.root, width = 500, height = 350, bg = "#14a3df")
        my_canvas.place(x = 470, y = 300)

        Typing_test_title = Label(my_canvas, text = "TYPING TEST", font = ("times new roman", 50, "bold"), bg = "yellow", fg = "red", bd = 10, relief = GROOVE)
        Typing_test_title.place(x = 0, y = 0, relwidth = 1)

        Rules_Lable = Label(my_canvas, text = "RULES :-", font = ("times new roman", 25), bg = "#14a3df")
        Rules_Lable.place(x = 30, y = 90)

        Rule_1 = Label(my_canvas, text = "1. YOU WILL BE GIVEN A SENTENCE.", font = ("times new roman", 20), bg = "#14a3df")
        Rule_1.place(x = 30, y = 130)

        Rule_2 = Label(my_canvas, text = "2. YOU WILL HAVE TO TYPE THAT SENTANCE.", font = ("times new roman", 20), bg = "#14a3df")
        Rule_2.place(x = 30, y = 170)

        Rule_3 = Label(my_canvas, text = "3. CLICK ON SUBMIT WHEN YOU FINISH.", font = ("times new roman", 20), bg = "#14a3df")
        Rule_3.place(x = 30, y = 210)

        Rule_4 = Label(my_canvas, text = "4. YOUR TOTAL TIME AND ACCURACY\nWILL BE SHOWN.", font = ("times new roman", 20), bg = "#14a3df")
        Rule_4.place(x = 30, y = 250)

        start_game_button = Button(my_canvas, text = "  START GAME  ", font = ("times new roman", 25, "bold"), relief = GROOVE, command = lambda:Create_New_Game())
        start_game_button.place(x = 60, y = 310)

        exit_button = Button(my_canvas, text = "   EXIT   ", font = ("times new roman", 25, "bold"), relief = GROOVE, command = lambda:Exit())
        exit_button.place(x = 340, y = 310)

def Start_Game():
    Game = Tk()
    Typing_Test(Game)
    Game.mainloop()

# Rules = Tk()
# Rules_Page(Rules)
# Rules.mainloop()