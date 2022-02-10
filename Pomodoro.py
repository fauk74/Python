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

timer=None

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

time_delay=10

reps=0

def start_timer():
        global reps
        reps+=1


        if reps==8 :

            count_down(LONG_BREAK_SEC)
            text.config(text="Break", fg=GREEN, bg=YELLOW,font=("Courier", 24, "bold"))

        elif reps % 2 == 0:
                count_down(SHORT_BREAK_SEC)
                text.config(text="Break", fg=GREEN, bg=YELLOW,font=("Courier", 24, "bold"))
        else:

                count_down(WORK_SEC)
                text.config(text="Work", fg=RED, bg=YELLOW, font=("Courier", 24, "bold"))



        print(reps)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    x=count//60
    y=count%60
    if y < 10:
        y="0"+str(y)
    z=str(x)+":"+str(y)
    canvas.itemconfig(text_timer, text=z)
    if count > 0:
        timer=window.after(time_delay,count_down, count-1)
    else:
        start_timer()
        mark=""
        work_session=reps%2
        for _ in range (0, work_session):
            mark+="✔"
        check_mark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

def update_label(x,y):
    sec_rem=(x-y)%60
    min_rem=(x-y)//60
    text_canv=str(min_rem)+":"+str(sec_rem)
    canvas.itemconfigure(text_timer, text=text_canv)



def ResetTimer():
    window.after_cancel(timer)
    canvas.itemconfig(text_timer, text="00:00")
    text.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps=0

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
text=Label(text="Timer", fg=GREEN, bg=YELLOW, font=("Courier",24,"bold"))

text.grid(column=1, row=0)
check_mark=Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1,row=4)

window.mainloop()
