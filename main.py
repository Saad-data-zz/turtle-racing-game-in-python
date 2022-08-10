from turtle import Turtle, Screen
import random
#timmy = Turtle
screen = Screen()
is_race_on = False
#to custimerize the size of window appear for turtle,
#500 and 400 means the pixels
#here we don"t know which one is height or width
#screen.setup(500, 400)
#so we needs to write explicatly
screen.setup(width=500, height=400)
user_bat = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "blue", "green", "yellow", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
#we have multiple instance in th list and each have different function
all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-238, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bat:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color ==user_bat:
                print(f"You've won! The {wining_color} turtle is the winner")
            else:
                print(f"You've lost! The {wining_color} turtle is the winner")


        ran_distance = random.randint(0, 10)
        turtle.forward(ran_distance)

screen.exitonclick()