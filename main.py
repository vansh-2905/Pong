from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle1 = Paddle(350, 0)

paddle2 = Paddle(-350,0)

def move_p1_up():
    paddle1.forward(20)

def move_p1_down():
    paddle1.back(20)

def move_p2_up():
    paddle2.forward(20)

def move_p2_down():
    paddle2.back(20)

screen.listen()
screen.onkey(move_p1_up, "Up")
screen.onkey(move_p1_down, "Down")
screen.onkey(move_p2_up, "w")
screen.onkey(move_p2_down, "s")

ball = Ball()


game_is_on = True

y_val = 10
x_val = 10
while game_is_on:
    time.sleep(0.07)
    screen.update()
    ball.move(x_val, y_val)

    if ball.ycor() == 280 or ball.ycor() == -280:
        y_val = ball.bounce(ball.ycor())

    if (ball.xcor() == 320 or ball.xcor() == -320) and (ball.distance(paddle1) < 51 or ball.distance(paddle2) < 51):
        x_val *= -1

    if ball.xcor() > 380 or ball.xcor() < -380:
        game_is_on = False
        print("Game is over")
    else:
        pass




screen.exitonclick()
