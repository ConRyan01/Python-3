from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=1500, height=400)
user_bet = screen.textinput(title='make your bet', prompt='which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

tim = Turtle(shape='turtle')
tom = Turtle(shape='turtle')
jim = Turtle(shape='turtle')
jon = Turtle(shape='turtle')
ben = Turtle(shape='turtle')
dan = Turtle(shape='turtle')
turtles = [tim, tom, jim, jon, ben, dan]

def set_color(turtle: Turtle, color: str):
    turtle.color(color)

def set_start_pos(turtle: Turtle, y_coord: int):
    turtle.penup()
    x_coord = -700
    turtle.goto(x_coord, y_coord)
    turtle.pendown()

for i in range(0, len(turtles)):
    set_color(turtles[i], colors[i])

y = -150
for i in range(0, len(turtles)):
    set_start_pos(turtles[i], y)
    y += 50

tim.goto(x=-230, y=0)

screen.exitonclick()