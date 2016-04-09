# This is a guess the number game.
import random
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

def getGuess():
    guess = 21
    try:
        guess = int(input())
        return guess
    except ValueError:
        print('please enter an integer')
        return None

# ask the player to guess 6 times
for guessesTaken in range (1,7):
    print('take a guess')
    #guess = 21
    guess = getGuess()

    if guess < secretNumber:
        print('your guess is too low')
    elif guess > secretNumber:
        print('your guess is too high')
    else:
        break  # this condition is the correct guess!

if guess == secretNumber:
    print('Good job!  You guess my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope.  The number I was thinking of was ' + str(secretNumber))

    
# Overall this works - however I'm not sure why the try:except bit is not working
#       if the except is triggered the program fails
