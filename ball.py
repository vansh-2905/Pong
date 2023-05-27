from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.up()
        self.speed(1)

    def move(self, x, y):
        x = self.xcor() + x
        y = self.ycor() + y
        self.goto(x,y)

    def bounce(self, y_ball):
        if y_ball == 280:
            y = -10
        if y_ball == -280:
            y = 10
        return y

