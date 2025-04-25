from instagram import data
import random

def format_data(account):
    account_name = account['name']
    return f"{account_name}"

def check_answer(user_guess, account_a, account_b):
    if account_a > account_b:
        return user_guess == 'a'
    else:
        return user_guess == 'b'

score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print("VS")
    print(f"Compare B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" *20)

    a_follower = account_a['followers']
    b_follower = account_b['followers']
    is_correct = check_answer(guess, a_follower, b_follower)

    if is_correct:
        score += 1
        print(f"You're correct, current score is {score}")
    else:
        print(f"Sorry you got it wrong, you scored {score}")
        game_should_continue = False