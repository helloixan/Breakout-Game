import turtle
import random

class Brick:
    def __init__(self, x, y, color):
        self.brick = turtle.Turtle()
        self.brick.speed(0)
        self.brick.shape("square")
        self.brick.color(color)
        self.brick.shapesize(stretch_wid=1, stretch_len=2.5)
        self.brick.penup()
        self.brick.goto(x, y)
        self.exists = True

    def destroy(self):
        if self.exists:
            self.brick.hideturtle()
            self.exists = False