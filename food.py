from turtle import Turtle
import random

BORDER_MIN = -270
BORDER_MAX = 270


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(BORDER_MIN, BORDER_MAX)
        random_y = random.randint(BORDER_MIN, BORDER_MAX)
        self.goto(random_x, random_y)
