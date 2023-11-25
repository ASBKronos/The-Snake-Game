from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        # We reduce the food size by halving it from 20 to 10 by multiplying length and width by 0.5
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')
        self.speed('fastest')
        self.new_food_loc()

    def new_food_loc(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)

