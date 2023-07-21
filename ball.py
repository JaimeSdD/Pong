from turtle import Turtle

MOVE_SPEED = 0.1

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = MOVE_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self, axis):
        if axis == "x":
            self.x_move *= -1
            self.move_speed *= 0.9
        elif axis == "y":
            self.y_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = MOVE_SPEED
        self.bounce("x")