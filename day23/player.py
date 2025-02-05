from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90) # direction-up
        self.move_distance = MOVE_DISTANCE
        self.penup()
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.goto(0, self.ycor() + self.move_distance)

    def go_back(self):
        self.goto(STARTING_POSITION)
