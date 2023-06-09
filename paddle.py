from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.move = 10
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=3.5, stretch_len=0.5)

    def move_up(self):
        if self.ycor() < 270:
            self.goto(self.xcor(), self.ycor()+10)

    def move_down(self):
        if self.ycor() > -270:
            self.goto(self.xcor(), self.ycor()-10)