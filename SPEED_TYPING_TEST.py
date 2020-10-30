from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from timeit import default_timer as timer
import random
import os
from difflib import SequenceMatcher

os.system("clear")

class Typing_Test:
    def __init__(self, root):
        self.root = root
        self.root.title("TYPING TEST")
        self.root.geometry("1440x880+0+0")

        self.bg_img = ImageTk.PhotoImage(file = "/Users/saniha/Dropbox/My Mac (niha का MacBook Air)/Desktop/NIKSH/IMAGES/BACKGROUNDS/bg_img_7.jpg")
        bg = Label(self.root, image = self.bg_img)
        bg.place(x = 0, y = 120)

        def Exit():
            self.root.destroy()

        def Accuracy_Checker():
            Question = random_word
            Answer = Answer_entry.get()

            Accuracy = (SequenceMatcher(a = Question, b = Answer).ratio()) * 100
            return Accuracy

        def Check_Answer():
            Answer = Answer_entry.get()
            End_Time = timer()
            Total_Time = End_Time - Start_Time
            Total_Accuracy = Accuracy_Checker()

            messagebox.showinfo("RESULT", "{} SECONDS\n\n{} % ACCURACY".format(Total_Time, Total_Accuracy))
            Exit()

        all_words = [
            "He ran out of money, so he had to stop playing poker.", 
            "The ants enjoyed the barbecue more than the family.", 
            "The fish listened intently to what the frogs had to say.", 
            "The stranger officiates the meal.", 
            "The minute she landed she understood the reason this was a fly-over state.", 
            "She lived on Monkey Jungle Road and that seemed to explain all of her strangeness.", 
            "Jeanne wished she has chosen the red button.", 
            "As he entered the church he could hear the soft voice of someone whispering into a cell phone.", 
            "They're playing the piano while flying in the plane.", 
            "Everyone says they love nature until they realize how dangerous she can be.", 
            "He hated that he loved what she hated about hate.", 
            "People who insist on picking their teeth with their elbows are so annoying!", 
            "The swirled lollipop had issues with the pop rock candy.", 
            "I love eating toasted cheese and tuna sandwiches.", 
            "He picked up trash in his spare time to dump in his neighbor's yard.", 
            "Italy is my favorite country; in fact, I plan to spend two weeks there next year.", 
            "There should have been a time and a place, but this wasn't it.", 
            "The virus had powers none of us knew existed.", 
            "For oil spots on the floor, nothing beats parking a motorbike in the lounge.", 
            "The teens wondered what was kept in the red shed on the far edge of the school grounds.", 
            "He excelled at firing people nicely.", 
            "Art doesn't have to be intentional.", 
            "She had a habit of taking showers in lemonade.", 
            "You can't compare apples and oranges, but what about bananas and plantains?", 
            "He fumbled in the darkness looking for the light switch, but when he finally found it there was someone already there.", 
            "Poison ivy grew through the fence they said was impenetrable.", 
            "Sometimes you have to just give up and win by cheating.", 
            "Nobody has encountered an explosive daisy and lived to tell the tale.", 
            "He was the type of guy who liked Christmas lights on his house in the middle of July.", 
            "She works two jobs to make ends meet; at least, that was her reason for not having time to join us.", 
            "I love bacon, beer, birds, and baboons.", 
            "They throw cabbage that turns your brain into emotional baggage.", 
            "Be careful with that butter knife.", 
            "His thought process was on so many levels that he gave himself a phobia of heights.", 
            "He went on a whiskey diet and immediately lost three days.", 
            "He stepped gingerly onto the bridge knowing that enchantment awaited on the other side.", 
            "Before he moved to the inner city, he had always believed that security complexes were psychological.", 
            "The knives were out and she was sharpening hers.", 
            "There's a message for you if you look up.", 
            "Nothing seemed out of place except the washing machine in the bar.", 
            "They got there early, and they got really good seats.", 
            "Wisdom is easily acquired when hiding under the bed with a saucepan on your head.", 
            "I thought red would have felt warmer in summer but I didn't think about the equator.", 
            "At that moment he wasn't listening to music, he was living an experience.", 
            "He wondered why at 18 he was old enough to go to war, but not old enough to buy cigarettes.", 
            "I'm a great listener, really good with empathy vs sympathy and all that, but I hate people.", 
            "When she didn’t like a guy who was trying to pick her up, she started using sign language.", 
            "He found the end of the rainbow and was surprised at what he found there.", 
            "He said he was not there yesterday; however, many people saw him there.", 
            "It doesn't sound like that will ever be on my travel list."
        ]

        random_generator = random.randint(0, len(all_words) - 1)
        random_word = all_words[random_generator]

        Start_Time = timer()

        title = Label(self.root, text = "TYPING TEST", font = ("times new roman", 100, "bold"), bg = "yellow", fg = "red", bd = 10, relief = GROOVE)
        title.place(x = 0, y = 0, relwidth = 1)

        my_canvas = Canvas(self.root, width = 1200, height = 350, bg = "#14a3df")
        my_canvas.place(x = 120, y = 300)

        my_canvas_2_0 = Canvas(my_canvas, width = 1100, height = 40, bg = "#14a3df")
        my_canvas_2_0.place(x = 50, y = 200)

        typing_test_title = Label(my_canvas, text = "TYPING TEST", font = ("times new roman", 50, "bold"), bg = "yellow", fg = "red", bd = 10, relief = GROOVE)
        typing_test_title.place(x = 0, y = 0, relwidth = 1)

        Question_Lable = Label(my_canvas, text = random_word, font = ("times new roman", 25), bg = "#14a3df")
        Question_Lable.place(x = 0, y = 120, relwidth = 1)

        Answer_entry = Entry(my_canvas_2_0, font = ("times new roman", 30), relief = GROOVE)
        Answer_entry.place(x = 0, y = 0, relwidth = 1)

        submit_button = Button(my_canvas, text = "   SUBMIT   ", font = ("times new roman", 30, "bold"), relief = GROOVE, command = lambda:Check_Answer())
        submit_button.place(x = 313, y = 290) # 160 Pixels

        exit_button = Button(my_canvas, text = "    EXIT    ", font = ("times new roman", 30, "bold"), relief = GROOVE, command = lambda:Exit())
        exit_button.place(x = 787, y = 290) # 100 Pixels

# game = Tk()
# Typing_Test(game)
# game.mainloop()