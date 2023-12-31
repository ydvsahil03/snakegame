from tkinter import *
import random

GAME_WIDTH = 800
GAME_HEIGHT = 800
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "GREEN"
FOOD_COLOR = "RED"
BACKGROUND_COLOR = "GREY"


class Snake:
    pass


class Food:
    pass


def next_turn():
    pass


def change_direction(new_direction):
    pass


def check_collision():
    pass


def game_over():
    pass


window = Tk()
window.title("snake game")
window.resizable(False, False)
score=0
direction='down'

label = Label(window, text="score: " + str(score), font="Arial")
label.pack()

canvas = Canvas(window, width=GAME_WIDTH, height=GAME_WIDTH, bg=BACKGROUND_COLOR)
canvas.pack()

window.update()
window_width = window.winfo_screenwidth()
window_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = ((screen_width - window_width) / 2)
y = ((screen_height - window_height) / 2)
window.geometry("%dx%d+%d+%d" % (window_width, window_height, x, y))
window.mainloop()
