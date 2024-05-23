from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")

colors=["red","blue","green","purple","yellow","orange"]
y_pos=[-70,-40,-10,20,50,80]
all_turtle=[]


for turtle_index in range(6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_pos[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_on=False
            win_color=turtle.pencolor()
            if win_color==user_bet:
                print(f"You've won! The {win_color} turtle is winner🤝")
            else:
                print(f"You've lost! The {win_color} turtle is winner😒")

        distance=random.randint(0,10)
        turtle.forward(distance)



screen.exitonclick()