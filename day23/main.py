import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move_up,"Up")
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_all()

    # Detect collision with finish line
    if player.ycor() > 280:
        player.go_back()
        scoreboard.level_up()
        car_manager.level_up()

    # Detect collision with left-side
    for car in car_manager.cars:
        if car.xcor() < -320:
            car.go_back()

    # Detect collision with cars
    for car in car_manager.cars:
        if player.distance(car) < 30 and (car.ycor() + 20 > player.ycor() > car.ycor() - 20):
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
