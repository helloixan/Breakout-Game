import turtle
from ball import Ball
from paddle import Paddle
from brick import Brick
import random

class Breakout:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Breakout Game")
        self.screen.bgcolor("black")
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)

        self.paddle = Paddle()
        self.ball = Ball()
        self.bricks = []
        self.score = 0
        self.game_over = False

        self.message = turtle.Turtle()
        self.message.color("white")
        self.message.penup()
        self.message.hideturtle()

        self.create_bricks()

        self.screen.listen()
        self.screen.onkeypress(self.paddle.move_left, "Left")
        self.screen.onkeypress(self.paddle.move_right, "Right")
        self.screen.onkeypress(self.restart, "r")

        self.update_game()

    def create_bricks(self):
        colors = ["red", "orange", "yellow", "green", "blue"]
        self.bricks.clear()
        for y in range(200, 300, 20):
            for x in range(-250, 260, 50):
                brick = Brick(x, y, random.choice(colors))
                self.bricks.append(brick)

    def update_game(self):
        if self.game_over:
            return

        self.ball.move()

        if self.ball.ball.xcor() > 290 or self.ball.ball.xcor() < -290:
            self.ball.bounce_x()
        if self.ball.ball.ycor() > 290:
            self.ball.bounce_y()
        if self.ball.ball.ycor() < -290:
            self.display_message("YOU LOSE!", self.score)
            self.game_over = True
            return

        # Deteksi tabrakan dengan paddle
        if (self.ball.ball.ycor() < -240 and self.ball.ball.ycor() > -250) and (
            self.paddle.paddle.xcor() - 50 < self.ball.ball.xcor() < self.paddle.paddle.xcor() + 50
        ):
            self.ball.bounce_y()

        for brick in self.bricks[:]:
            if brick.exists and self.ball.ball.distance(brick.brick) < 25:
                brick.destroy()
                self.bricks.remove(brick)
                self.ball.bounce_y()
                self.score += 1
                if not any(b.exists for b in self.bricks):
                    self.display_message("YOU WIN!", self.score)
                    self.game_over = True
                break

        self.screen.update()
        self.screen.ontimer(self.update_game, 10)

    def display_message(self, text, score):
        self.message.clear()
        self.message.goto(0, 0)
        self.message.write(
            f"{text}\nScore: {score}\nPress 'R' to Restart", align="center", font=("Arial", 16, "bold")
        )

    def restart(self):
        self.message.clear()
        self.ball.reset_position()
        self.score = 0
        self.game_over = False
        self.create_bricks()
        self.update_game()