# In the day 6 the project is focused in the Reeborg's World, a game that you can play in the website https://reeborg.ca/reeborg.html
# The goal of the game is to escape the maze, and the code below is the solution for this problem.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    elif wall_in_front():
        turn_left()

# The code above is the solution for the problem, but the code below is the solution for the challenge of the day 6.
# The challenge is to create a function that can turn the robot in the direction that you want, and the code below is the solution for this problem.

def turn(direction):
    if direction == "right":
        turn_right()
    elif direction == "left":
        turn_left()
    elif direction == "back":
        turn_left()
        turn_left()
    else:
        print("Invalid direction")

# The code below is the solution for the problem, but the code below is the solution for the challenge of the day 6.
# The challenge is to create a function that can move the robot in the direction that you want, and the code below is the solution for this problem.
        
def move(direction):
    if direction == "forward":
        move()
    elif direction == "backward":
        turn("back")
        move()
    else:
        print("Invalid direction")