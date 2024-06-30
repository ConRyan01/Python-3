from turtle import Turtle
from time import sleep

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: {self.score}', align = ALIGNMENT, font = FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write("GAME OVER!", align = ALIGNMENT, font = FONT)

    def set_speed(self):
        speed = 0.1
        if self.score > 9 and self.score < 20:
            speed = 0.08
        elif self.score > 19 and self.score < 30:
            speed = 0.05
        elif self.score > 29 and self.score < 40:
            speed = 0.03
        elif self.score > 39:
            speed = 0.01

        return sleep(speed)
            

        
