import random, sys

gameChoices = ['paper','scissors','rock']
wins = 0
ties = 0
losses = 0
while True:
    print('Lets play a game.\n'
            'Rock, Paper Scissors')
    while True:
        print('ties: '+ str(ties)+', '+ 'wins: ' + str(wins)+ ', ' +  'losses' + str(losses))
        computerGuess = random.choice(gameChoices)
        print(computerGuess)
        playerGuess = input('what is your choice? (Rock, Paper, Scissors or Quit) ').lower()
        
        if playerGuess == 'quit':
            sys.exti()
        elif playerGuess == computerGuess:
            print('Tie')
            ties += 1
        elif playerGuess == 'rock' and computerGuess == 'paper':
            print('You lose')
            losses += 1
        elif playerGuess == 'rock' and computerGuess == 'scissors':
            print('You win')
            wins += 1
        elif playerGuess == 'paper' and computerGuess == 'scissors':
            print('You lose')
            losses += 1
        elif playerGuess == 'paper' and computerGuess == 'rock':
            print('You win')
            wins += 1
        elif playerGuess == 'scissors' and computerGuess == 'rock':
            print('You lose')
            losses += 1
        elif playerGuess == 'scissors' and computerGuess == 'paper':
            print('You win')
            wins += 1
        else:
            print('sorry, not one of your options.')

        