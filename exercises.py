
#GUESS THE NUMBER
import random

def get_random_number():
    lower = int(input('What is the lowest number? '))
    upper = int(input('What is the highest number? '))
    random_number = round(random.randrange(lower, upper))
    return random_number

def player_guess():
    turn = int(input('what is your guess? '))
    return turn


def play_round():
    num_guesses = 0
    game_number = get_random_number()
    turn = player_guess()
    while True:
        if game_number == turn:
            num_guesses +=1
            print('You win!')
            break
        elif game_number > turn:
            num_guesses +=1
            print('Your guess is too low')
            turn = player_guess()
        elif game_number < turn:
            num_guesses +=1
            print('Your guess is too high')
            turn = player_guess()
        else:
            print('Please enter a valid number. (i.e. 1)')
    return num_guesses




def start_game():
    print('Lets Play a guessing game.')
    while True:
        new_game = "yes"
        if new_game == "yes":
            play_round()
            new_game = input("Would you like to play again? (Yes or No)").lower()
        elif new_game == "no":
            break
        else:
            print('thanks for playing')
            break


start_game()
















# NAME AND AGE EXERCISE
# name = input('Hello, What is your name? ')
# print(f'Hello {name}. It is nice to meet you. the length of your name is {len(name)}')
# age = int(input('What is your age?'))
# print(f'You will be {age +1} in a year.')
