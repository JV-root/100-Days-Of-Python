"""
The program will choose a random word from a list of words.
The program will display the spaces for the letters in the word.
The user will guess letters.
If the user guesses a letter that is in the word, the letter will appear in the correct blank space.
If the user guesses a letter that is not in the word, the user loses a life.
If the user fills in all the blanks before they run out of lives, they win.
If the user runs out of lives before all the blanks are filled in, they lose.

i make a little improvement in the code in compare to the original game, i add a list of words from a api, so the game will be more fun, because the words will be random.

"""

import random


from hangman_words_api import get_words

word_list = get_words()

print(word_list)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


from hangman_art import logo
print(logo)


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()


    if guess in display:
        print(f"You've already guessed {guess}")


    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter


    if guess not in chosen_word:

        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")


    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    from hangman_art import stages
    print(stages[lives])