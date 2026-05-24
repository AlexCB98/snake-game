from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('green')
        self.speed('fastest')
        x = randint(-280, 280)
        y = randint(-280, 280)
        self.goto(x, y)