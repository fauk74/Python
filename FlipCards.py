import random

import pandas as pd
from tkinter import *
import time
import json

#-----------------VARIABLES
BACKGROUND_COLOR = "#B1DDC6"
LANG1="French"
LANG2="English"
word="word"
current_card={}

try:
    df=pd.read_csv("data/words_to_learn.json")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")


to_learn=df.to_dict(orient="records")




def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_background, image=card_front)
    word=current_card['French']
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(parola, text=word, fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(card_title,  text="English", fill="white")
    canvas.itemconfig(parola,  text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)

def right_next():
    global to_learn, current_card
    to_learn.remove(current_card)
    with open(file="data/words_to_learn.json", mode="w") as file:
        json.dump(to_learn, file, indent=4)
    next_word()


window =Tk()
window.title("Flip Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flashy")

flip_timer=window.after(3000, func=flip_card)


#--------------------load images
right = PhotoImage(file="images/right.png")
wrong=PhotoImage(file="images/wrong.png")
wrong=PhotoImage(file="images/wrong.png")
card_back=PhotoImage(file="images/card_back.png")
card_front=PhotoImage(file="images/card_front.png")

canvas=Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background= canvas.create_image(400,263, image=card_front)
card_title=canvas.create_text(400,150, text="Title", font=("Ariel",40,"italic"))
parola=canvas.create_text(400,263,text="word", font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
#canvas.create_image(400,263, image=card_back)
canvas.grid(column=0,row=0, columnspan=2)



label_lang=Label(window, text=LANG1,  bg="black", font=("Arial", ))
label_word=Label(window, text=word,  bg="black")

button1=Button(image=right, highlightthickness=0, command=right_next)
button1.grid(column=0, row=1)

button2=Button(image=wrong, highlightthickness=0, command=next_word)
button2.grid(column=1, row=1)


next_word()

window.mainloop()

