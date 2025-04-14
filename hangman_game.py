import random
from hangman_words import word_list

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("guess the letter: \n").lower()

    if guess in correct_letters:
        print(f"You've guessed {guess}")

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, thats not in the word")
        if lives == 0:
            game_over = True
            print("You lose!")

    if "_" not in display:
        game_over = True
        print("You Win!")

    print(lives)