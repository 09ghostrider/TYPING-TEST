from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from timeit import default_timer as timer
import random
import os

os.system("clear")

class Typing_Test:
    def __init__(self, root):
        self.root = root
        self.root.title("TYPING TEST")
        self.root.geometry("1440x880+0+0")

        self.bg_img = ImageTk.PhotoImage(file = "/Users/saniha/Dropbox/My Mac (niha का MacBook Air)/Desktop/bg_img_7.jpg")
        bg = Label(self.root, image = self.bg_img)
        bg.place(x = 0, y = 120)

        def Exit():
            self.root.destroy()

        def Check_Answer():
            Answer = Answer_entry.get()
            
            if Answer == random_word:
                End_Time = timer()
                Total_Time = End_Time - Start_Time
                messagebox.showinfo("RESULT", "YOU TOOK A TOTAL OF\n{}\nSECONDS".format(Total_Time))
                Exit()

            else:
                messagebox.showinfo("ERROR", "INVALID WORD")

        all_words = ["Programming", "Coding", "Algorithm", "Systems", "Python", "Software", "Mac Book Air", "Windows"]

        random_generator = random.randint(0, len(all_words) - 1)
        random_word = all_words[random_generator]

        Start_Time = timer()

        title = Label(self.root, text = "TYPING TEST", font = ("times new roman", 100, "bold"), bg = "yellow", fg = "red", bd = 10, relief = GROOVE)
        title.place(x = 0, y = 0, relwidth = 1)

        my_canvas = Canvas(self.root, width = 500, height = 350, bg = "#14a3df")
        my_canvas.place(x = 470, y = 300)

        typing_test_title = Label(my_canvas, text = "TYPING TEST", font = ("times new roman", 50, "bold"), bg = "yellow", fg = "red", bd = 10, relief = GROOVE)
        typing_test_title.place(x = 0, y = 0, relwidth = 1)

        Question_Lable = Label(my_canvas, text = random_word, font = ("times new roman", 30), bg = "#14a3df")
        Question_Lable.place(x = 0, y = 120, relwidth = 1)

        Answer_entry = Entry(my_canvas, font = ("times new roman", 30), relief = GROOVE)
        Answer_entry.place(x = 100, y = 200)

        submit_button = Button(my_canvas, text = "   SUBMIT   ", font = ("times new roman", 30, "bold"), relief = GROOVE, command = lambda:Check_Answer())
        submit_button.place(x = 60, y = 290) # 160 Pixels

        exit_button = Button(my_canvas, text = "    EXIT    ", font = ("times new roman", 30, "bold"), relief = GROOVE, command = lambda:Exit())
        exit_button.place(x = 310, y = 290) # 100 Pixels

# game = Tk()
# Typing_Test(game)
# game.mainloop()