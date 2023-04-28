import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# import time
# count=6
# while True:
#     time.sleep(1)
#     count-=1


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        for i in range(0, reps//2):
            mark += "✓"

        label2.config(text=mark)
        label2.grid(column=1, row=4)


def reset_timer():
    window.after_cancel(timer)
    label.config(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="Work", fg=GREEN)


window = Tk()
window.title("Pomodoro")
window.minsize(width=400, height=400)
window.config(padx=50, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white',
                                font=(FONT_NAME, 33, "bold"))

canvas.grid(column=1, row=1)


start_btn = Button(window, text="Start", width=10,
                   highlightthickness=0, command=start_timer)
reset_btn = Button(window, text="Reset", width=10,
                   highlightthickness=0, command=reset_timer)
start_btn.grid(column=0, row=3)
reset_btn.grid(column=2, row=3)

# button

label = Label(window, text="Timer", font=(
    FONT_NAME, 37, "bold"), highlightthickness=0, fg=GREEN, bg=YELLOW)
label.grid(column=1, row=0)

label2 = Label(window, text="✓", fg=GREEN, bg=YELLOW,
               font=(FONT_NAME, 20, "bold"))


# labels


window.mainloop()
