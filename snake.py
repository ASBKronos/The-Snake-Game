import turtle
from turtle import Turtle
import time

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_STEP = 20


class Snake:
    '''Creates a snake of size 3 initially which moves in the right direction'''
    def __init__(self):
        self.snake_body = []
        for i in START_POS:
            self.create_snake()
            self.body.goto(i)  # Uses both x and y coordinates from global variable START_POS

        self.head = self.snake_body[0]

    # Creating the snake body (with three turtle squares lined up next to each other)
    def create_snake(self):
        self.body = Turtle('square')
        self.body.color("white")
        self.body.penup()
        self.snake_body.append(self.body)

    def move(self):
        # Move third piece(index 2) to second position(piece at index 1) and second piece to first position(piece at index 0)
        for i in range(len(self.snake_body) - 1, 0,-1):
            new_x = self.snake_body[i - 1].xcor()
            new_y = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(new_x, new_y)
        self.head.forward(MOVE_STEP) # Initially the head starts moving right on screen by 20 paces

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)