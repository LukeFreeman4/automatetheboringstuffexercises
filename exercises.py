

#! coin flip
import random







#! Comma Code
# list_one = ['apples', 'cats','tofu','bananas', 'maps']

# def list_to_string(arg):
#     new_string = ''
#     for i in range(len(arg) - 1):   
#         new_string += (arg[i] + ', ')
#     new_string += ('and ' + arg[-1])
#     return new_string

# print(list_to_string(list_one))  
        

#! Collatz Sequience -then keep calling collatz on the number until the value is 1
# def collatz(number):
#     while number > 1:
#         if number % 2 == 0:
#             number = number // 2
#             print(number)
#         elif number % 2 == 1:
#             number = (3 * number + 1)
#             print(number)


# collatz(130)

#!ZIGZAG PROGRAM
# import time, sys
# indent = 0
# indent_increasing = True

# try:
#     while True:
#         print(' ' * indent, end='')
#         print('**********')
#         time.sleep(0.1)

#         if indent_increasing:
#             indent = indent + 1
#             if indent == 20:
#                 indent_increasing = False
#         else:
#             indent = indent -1
#             if indent == 0:
#                 indent_increasing = True

# except KeyboardInterrupt:
#     sys.exit()


#!GUESS THE NUMBER -- Still couldn't get the game to keep track of high score with using functions nor print my exit message when player is done with the game. 
# import random

# def get_random_number():
#     lower = int(input('What is the lowest number? '))
#     upper = int(input('What is the highest number? '))
#     random_number = round(random.randrange(lower, upper))
#     return random_number

# def player_guess():
#     turn = int(input('what is your guess? '))
#     return turn

# def play_round():
#     num_guesses = 0
#     game_number = get_random_number()
#     turn = player_guess()
#     while True:
#         if game_number == turn:
#             num_guesses +=1
#             print('You win!')
#             break
#         elif game_number > turn:
#             num_guesses +=1
#             print('Your guess is too low')
#             turn = player_guess()
#         elif game_number < turn:
#             num_guesses +=1
#             print('Your guess is too high')
#             turn = player_guess()
#         else:
#             print('Please enter a valid number. (i.e. 1)')
#     return num_guesses


# def start_game():
#     print('Lets Play a guessing game.')
#     new_game = 'yes'
#     while new_game == 'yes':
#         if new_game == 'yes': 
#             play_round()
#             new_game = input("Would you like to play again? (Yes or No)").lower()
#         elif new_game == "no":
#             print('Thanks for playing')
#             break
#         else:
#             print('please enter a valid option')
#             new_game = input("Would you like to play again? (Yes or No)").lower()

# start_game()

#! NAME AND AGE EXERCISE
# name = input('Hello, What is your name? ')
# print(f'Hello {name}. It is nice to meet you. the length of your name is {len(name)}')
# age = int(input('What is your age?'))
# print(f'You will be {age +1} in a year.')
