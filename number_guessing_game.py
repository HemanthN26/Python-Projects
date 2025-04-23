import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0

def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high")
        return turns -1
    if user_guess < actual_answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! the answer was {actual_answer}")

def set_difficulty():
    level = input("You want it to be 'hard' or 'easy': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 to 100.")
    answer = random.randint(1, 100)

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You ran outta guesses, you lose")
            return

game()