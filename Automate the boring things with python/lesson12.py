import random

print ('Hello, What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between one and twenty')
secretNumber = random.randint(1, 20)

#print ('DEBUG: Secret number is ' + str(secretNumber))

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int (input())
    if guess < secretNumber:
        print('You guess is too low.')
    elif guess > secretNumber:
        print('You guess is too high.')
    else:
        break

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope, The number I was thinking of was' + str(secretNumber))