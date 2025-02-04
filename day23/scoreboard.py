from turtle import Turtle


FONT = ("Courier", 24, "normal")
SCOREBOARD_POSITION = (-270, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(SCOREBOARD_POSITION)
        self.draw_score()

    def draw_score(self):
        self.write(arg=f"Level: {self.level}", move=False, align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.draw_score()

    def game_over(self):
        self.home()
        self.write(arg="Game Over", move=False, align="center", font=FONT)
