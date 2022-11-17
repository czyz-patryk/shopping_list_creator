import json
from tkinter import *
from tkinter import messagebox
import pyperclip
import os

from shopping_list_functions import *

# -------------------- COLOURS

BACK_COLOR = "#3F72AF"
FONT_COLOR = "#DBE2EF"
TITLE = "#112D4E"

# -------------------- OPEN FILE WITH PRODUCTS

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "diet.json")
file = open(file_path)
data = json.load(file)

# -------------------- CREATE CLASS OBJECT

slf = ShoppingListFunctions()


# -------------------- BUTTONS' FUNCTIONS

def make_and_copy_to_clipboard():
    pyperclip.copy(slf.make_shopping_list(data))
    messagebox.showinfo("Info", "Your list is copied to clipboard. \n Now You can paste it to notepad")


def delete_list():
    slf.shopping_list.clear()
    messagebox.showinfo("Info", "Your shopping list is empty")
    slf.list_of_vars.clear()


def close():
    window.destroy()


def close_win(e):
    window.destroy()


# -------------------- CREATE GRAPHICAL USER INTERFACE

window = Tk()

# --- Title & configuration

window.config(padx=25, pady=25, bg=BACK_COLOR)
window.title("SHOPPING LIST MANAGER")

Label(text="SHOPPING LIST MANAGER", bg=BACK_COLOR, fg=TITLE, font=("helvetica", 50, "bold")) \
    .grid(row=0, column=0, columnspan=9, pady=20)

# --- Day's names

for r in range(2, 15, 2):
    day = int(r / 2 - 1)
    Label(text=slf.week_days[day], bg=BACK_COLOR, fg=FONT_COLOR, font=("arial", 35, "italic")) \
        .grid(row=r, column=0, rowspan=2, pady=8, padx=8, sticky=E)

# --- Meal's names

for c in range(1, 8, 2):
    meal = int(c / 2 - 0.5)
    Label(text=slf.meals[meal], bg=BACK_COLOR, fg=FONT_COLOR, font=("arial", 30, "italic")) \
        .grid(row=1, column=c, columnspan=2, padx=10, pady=4, sticky=S)

# --- User's names

for c in range(1, 8, 2):
    for r in range(2, 16, 2):
        patryk = Label(text="User 1", bg=BACK_COLOR, fg=FONT_COLOR, font=("arial", 15))
        patryk.grid(row=r, column=c, padx=10, sticky=SE)

for c in range(2, 9, 2):
    for r in range(2, 16, 2):
        bartek = Label(text="User 2", bg=BACK_COLOR, fg=FONT_COLOR, font=("arial", 15))
        bartek.grid(row=r, column=c, padx=10, sticky=SW)

# --- Checkboxes

i = 0
for r in range(3, 16, 2):
    for c in range(1, 9):
        slf.list_of_vars.append(IntVar(value=0))
        check_button = Checkbutton(variable=slf.list_of_vars[i], onvalue=1, offvalue=0, bg=BACK_COLOR, height=1, width=2)
        check_button.grid(row=r, column=c, sticky=N)
        i += 1

# --- Buttons

Button(text="Confirm & Copy", fg=TITLE, borderwidth=0, font=("arial", 30, "italic"), command=make_and_copy_to_clipboard) \
    .grid(row=16, column=1, columnspan=4, pady=20)

Button(text="Reset", fg=TITLE, borderwidth=0, font=("arial", 30, "italic"), command=delete_list) \
    .grid(row=16, column=5, columnspan=2, pady=20)

Button(text="Exit", fg=TITLE, borderwidth=0, font=("arial", 30, "italic"), command=close) \
    .grid(row=16, column=7, columnspan=2)

# -------------------- CLOSE GRAPHICAL USER INTERFACE

window.bind('<Escape>', lambda e: close_win(e))
window.mainloop()
