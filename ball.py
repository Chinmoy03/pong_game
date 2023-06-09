from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.setheading(135)
        self.color("white")

    def reset(self):
        self.goto(0, -285)
        # top is 293 limit

    def move(self):
        self.forward(7)
