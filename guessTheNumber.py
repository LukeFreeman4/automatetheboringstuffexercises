import random, sys, os, math

randomNum = random.randint(1,20)
print('I\'m thinking of a number between 1 and 20.' 
      )
count = 1
guess = guess = int(input('Guess the number: '))
while guess != randomNum:
    guess = int(input('Guess the number: '))
  if guess > randomNum:
    print('Your guess is too high')
  elif guess < randomNum:
    print('Your guess is too low')
  count += 1
print('it took you ' + str(count) + ' tries')