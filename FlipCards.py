
import pandas as pd
from tkinter import *

df=pd.read_csv("data/french_words.csv")
window =Tk()

right = PhotoImage(file="images/right.png")
wrong=PhotoImage(file="images/wrong.png")
wrong=PhotoImage(file="images/wrong.png")
card_back=PhotoImage(file="images/card_back.png")
card_front=PhotoImage(file="images/card_front.png")


BACKGROUND_COLOR = "#B1DDC6"
LANG1="French"
LANG2="English"
word="word"

window.title("Flip Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas=Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

canvas.create_image(400,263, image=card_back)
canvas.grid(column=0,row=1, columnspan=2)


label_lang=Label(window, text=LANG1,  bg="black", font=("Arial", ))
label_word=Label(window, text=word,  bg=word)

button1=Button(image=right, highlightthickness=0)
button1.grid(column=1, row=2)

button2=Button(image=wrong, highlightthickness=0)
button2.grid(column=0, row=2)


window.mainloop()

