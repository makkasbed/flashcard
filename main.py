BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random

selected_word= {}


def correct():
    words.remove(selected_word)
    next_card()
    df = pandas.DataFrame(words)
    df.to_csv("data/words_to_learn.csv",index=False)


def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=selected_word['English'], fill="white")
    canvas.itemconfig(card_bg, image=image_back)
    window.after(3000, func=flip_card)


def next_card():
    global selected_word, flip_timer
    window.after_cancel(flip_timer)

    selected_word = random.choice(words)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=selected_word['French'], fill="black")
    canvas.itemconfig(card_bg, image=image_front)
    flip_timer = window.after(3000, func=flip_card)


try:
   words_df = pandas.read_csv("data/words_to_learn.csv")
   words = words_df.to_dict(orient="records")
except FileNotFoundError:
    words_df = pandas.read_csv("data/french_words.csv")
    words = words_df.to_dict(orient="records")
else:
    words = words_df.to_dict(orient="records")

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

image_front = PhotoImage(file="images/card_front.png")
image_back = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526)
card_bg = canvas.create_image(400, 263, image=image_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

title = canvas.create_text(400, 150, font=('Arial', 40, 'italic'))
word = canvas.create_text(400, 263, font=('Arial', 60, 'italic'))
canvas.grid(row=0, column=0, columnspan=2)


wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0,command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=correct)
right_button.grid(row=1, column=1)


next_card()

window.mainloop()



