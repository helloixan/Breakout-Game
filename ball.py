import turtle
import random

class Ball:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed(40)
        self.ball.shape("circle")
        self.ball.color("red")
        self.ball.penup()
        self.ball.goto(0, -230)
        self.ball.dx = random.choice([-2, 2])
        self.ball.dy = 2
    
    def move(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)
    
    def bounce_x(self):
        self.ball.dx *= -1
    
    def bounce_y(self):
        self.ball.dy *= -1
    
    def reset_position(self):
        self.ball.goto(0, -230)
        self.bounce_y()