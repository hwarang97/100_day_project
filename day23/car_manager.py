from random import choice
from random import randint
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_AMOUNT = 30
CREATE_UNDER_LINE = -230
CAR_X_RANGE = (-290, 290)
CAR_Y_RANGE = (-230, 290)


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.color(choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.setheading(180)
        self.move_speed = STARTING_MOVE_DISTANCE
        self.penup()
        self.go_back()

    def move(self):
        self.forward(self.move_speed)

    def go_back(self):
        self.goto(320,randint(*CAR_Y_RANGE))


class CarManager:
    def __init__(self):
        self.cars = []
        self.create_car_randomly()

    def create_car_randomly(self):
        for _ in range(CAR_AMOUNT):
            car = Car()
            self.cars.append(car)
            car.goto(randint(*CAR_X_RANGE), randint(*CAR_Y_RANGE))
            car.move()

    def move_all(self):
        for car in self.cars:
            car.move()

    def level_up(self):
        for car in self.cars:
            car.move_speed += MOVE_INCREMENT
