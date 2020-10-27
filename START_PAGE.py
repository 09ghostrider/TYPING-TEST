from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from timeit import default_timer as timer
import random
import os
from SPEED_TYPING_TEST import *

os.system("clear")

class Start_Game_Class:
    def __init__(self, root):
        self.root = root
        self.root.title("TYPING TEST")
        self.root.geometry("1440x880+0+0")

        self.bg_img = ImageTk.PhotoImage(file = "/Users/saniha/Dropbox/My Mac (niha का MacBook Air)/Desktop/bg_img_7.jpg")
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

        typing_test_title = Label(my_canvas, text = "TYPING TEST", font = ("times new roman", 50, "bold"), bg = "yellow", fg = "red", bd = 10, relief = GROOVE)
        typing_test_title.place(x = 0, y = 0, relwidth = 1)

        Question_Lable = Label(my_canvas, text = "DO YOU WANT TO BEGIN\nTHE TEST?", font = ("times new roman", 30), bg = "#14a3df")
        Question_Lable.place(x = 70, y = 120)

        yes_button = Button(my_canvas, text = "   YES   ", font = ("times new roman", 30, "bold"), relief = GROOVE, command = lambda:Create_New_Game())
        yes_button.place(x = 100, y = 270) # 100 Pixels

        no_button = Button(my_canvas, text = "    NO    ", font = ("times new roman", 30, "bold"), relief = GROOVE, command = lambda:Exit())
        no_button.place(x = 300, y = 270) # 100 Pixels

def Start_Game():
    Game = Tk()
    Typing_Test(Game)
    Game.mainloop()

Start = Tk()
Start_Game_Class(Start)
Start.mainloop()