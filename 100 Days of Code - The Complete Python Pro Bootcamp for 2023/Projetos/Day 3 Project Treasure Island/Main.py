# Day 3 Project Treasure Island
"""

Make your own "Choose Your Own Adventure" game. Use conditionals such as if, else, and elif statements to lay out the logic and the story's path in your program.

To write your code according to my story, you can use this flow chart from draw.io to help you.

However, I think the fun part is writing your own story 😊

🧞‍♂️ 🐊 🧙‍♂️ 🧟 🧚‍♂️ 🧝‍♂️ 🥷 🤖 👽 🙀

That said if you'd like to continue with my example, feel free to use the text snippets below...

Text Snippets from my example
'You're at a crossroad. Where do you want to go? Type "left" or "right"'
'You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'
"You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"
"It's a room full of fire. Game Over."
"You found the treasure! You Win!"
"You enter a room of beasts. Game Over."
"You chose a door that doesn't exist. Game Over."
"You get attacked by an angry trout. Game Over."
"You fell into a hole. Game Over."


"""


print('Welcome to Treasure Island.')
print('Your mission is to find the treasure.')

choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".\n').lower()
if choice1 == 'left':
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a '
                    'boat. Type "swim" to swim across.\n').lower()
    if choice2 == 'wait':
        choice3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one '
                        'blue. Which colour do you choose?\n').lower()
        if choice3 == 'red':
            print('It\'s a room full of fire. Game Over.')
        elif choice3 == 'yellow':
            print('You found the treasure! You Win!')
        elif choice3 == 'blue':
            print('You enter a room of beasts. Game Over.')
        else:
            print('You chose a door that doesn\'t exist. Game Over.')
    else:
        print('You got attacked by an angry trout. Game Over.')