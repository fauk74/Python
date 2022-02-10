from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
WORK_SEC=WORK_MIN*60
SHORT_BREAK_SEC=SHORT_BREAK_MIN*60
LONG_BREAK_SEC=LONG_BREAK_MIN*60

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    count_down(5)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    canvas.itemconfig(text_timer, text=count)
    if count > 0:
        window.after(1000,count_down, count-1)
# ---------------------------- UI SETUP ------------------------------- #

def update_label(x,y):
    sec_rem=(x-y)%60
    min_rem=(x-y)//60
    text_canv=str(min_rem)+":"+str(sec_rem)
    canvas.itemconfigure(text_timer, text=text_canv)



# def StartTimer():
 #   for repeat in range (0,4):
 #       for looping1 in range (0,WORK_SEC):
 #           time.sleep(1)
 #           update_label( WORK_SEC, looping1)
 #       for looping2 in range (0,SHORT_BREAK_SEC):
 #           time.sleep(1)
 #           update_label( SHORT_BREAK_SEC, looping2)
 #   for looping3 in range(0, LONG_BREAK_SEC):
 #       time.sleep(1)
 #       update_label(LONG_BREAK_SEC, looping3)

def ResetTimer():
    pass

window=Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



canvas=Canvas(width=200, height=224, bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
canvas.grid(column=1,row=1)
text_timer=canvas.create_text(100,132,text="00:00", fill="white", font=("Courier", 24,"bold"))

button1=Button(text="Start",command=start_timer)
button1.grid(column=0,row=3)
button2=Button(text="Reset",command=ResetTimer)
button2.grid(column=3,row=3)
text=Label(text="Timer", fg=GREEN, font=("Courier",24,"bold"))
text=Label(text="Timer", fg=GREEN, font=("Courier",24,"bold"))
text.grid(column=1, row=0)


window.mainloop()
