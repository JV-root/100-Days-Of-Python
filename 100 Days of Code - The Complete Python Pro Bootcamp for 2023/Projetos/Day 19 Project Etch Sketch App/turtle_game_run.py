from turtle import Turtle, Screen
import random
import random


tim = Turtle()
screen = Screen()
screen.setup(width=1920, height=1080)

user_bet = screen.textinput(title = 'Make your bet', prompt= 'Which turtle will win the race? Enter a color: ')

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=-100 + turtle_index * 30)
    all_turtles.append(new_turtle)



if user_bet:
    is_racer_on = True
    

while is_racer_on:
    
    for turtle in all_turtles:
        
        
        if turtle.xcor() > 230:
            is_racer_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You won! The {winning_color} turtle is the winner!')
            else:
                print(f'You lost! The {winning_color} turtle is the winner!')
        
        
        
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
    
    

screen.exitonclick()