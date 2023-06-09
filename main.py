from turtle import Screen, Turtle
from paddle import Paddle
import time
from ball import Ball

# Create the screen and appropriate features
screen = Screen()
screen.bgcolor("black")
screen.title("PONG GAME")
screen.setup(width=800, height=600)
screen.tracer(0)
# create a turtle to draw on the screen
draw = Turtle()
draw.hideturtle()
draw.penup()
draw.goto(0, 300)
draw.pendown()
draw.pensize(5)
draw.setheading(270)
draw.pencolor("white")
for i in range(300, -300, -40):
    draw.forward(20)
    draw.penup()
    draw.forward(20)
    draw.pendown()
screen.update()

# to create the two paddles and send them to their locations
left_paddle = Paddle()
left_paddle.goto(-380, 0)
# right_paddle = Paddle()
# right_paddle.goto(380, 0)
ball = Ball()
ball.reset()
screen.listen()
screen.onkeypress(fun=left_paddle.move_up, key="w")
screen.onkeypress(fun=left_paddle.move_down, key="s")
screen.update()

while True:
    ball.move()
    # constant move the right paddle
    # if right_paddle.ycor() > 270:
    #     right_paddle.move = -10
    # elif right_paddle.ycor() < -270:
    #     right_paddle.move = 10
    # right_paddle.goto(right_paddle.xcor(), right_paddle.ycor() + right_paddle.move)

    # detect collision of the ball with paddles
    if ball.xcor() <= -370:
        if left_paddle.ycor() + 40 >= ball.ycor() >= left_paddle.ycor() - 40:
            if 90 < ball.heading() < 180:
                ball.hideturtle()
                ball.setheading(180 - ball.heading())
                ball.showturtle()
            elif 180 < ball.heading() < 270:
                ball.hideturtle()
                ball.setheading(180 - ball.heading())
                ball.showturtle()
            elif ball.heading() == 180:
                ball.setheading(0)
        if ball.xcor() <= -385:
            print(ball.xcor())
            break
    elif ball.xcor() >= 370:
        if 0 < ball.heading() < 90:
            ball.hideturtle()
            ball.setheading(180 - ball.heading())
            ball.showturtle()

        elif 270 < ball.heading() < 360:
            ball.hideturtle()
            ball.setheading(180 - ball.heading())
            ball.showturtle()
        elif ball.heading() == 0:
            ball.setheading(180)

    # detect collision with the walls
    if ball.ycor() >= 293 or ball.ycor() <= -285:
        ball.setheading(360 - ball.heading())

    time.sleep(0.02)
    screen.update()

screen.mainloop()
