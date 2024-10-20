from random import randint


EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5
#Choosing a number between 1 and 100
def check_answer(user_guess,actual_answer,turns):
    """checks answer against guess returs the number of turns remaining"""
    if user_guess > actual_answer:
        print("TOO HIGH")
        return turns - 1
    elif user_guess < actual_answer:
        print("TOO LOW")
        return turns - 1
    else:
        print(f"The actual answer is {actual_answer}")
        print("You WIN")
#funtion to set difficulty
def set_difficulty():
    level = input("CHOOSSEEE 'EASY' or 'HARD' ")
    if level == "easy":
        return EASY_LEVEL_TURN
    elif level == "hard":
        return HARD_LEVEL_TURN
#Function to check users guess against actual answer
def game():
    print("WELCOME TO THE GUESSING GAME")
    print("im thinking of a number from 1 to 100")
    answer = randint(1,100)
    print(f"The actual answer is {answer}")
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} number of attempts")
        guess = int(input("Guess a number: "))
        turns = check_answer(guess, answer , turns)
        if turns == 0:
           print("You Run out of turns you loose")
           return
        elif guess != answer:
            print("Guess again")

game()
