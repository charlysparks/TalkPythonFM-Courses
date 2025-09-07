import random

print('----------------------------------')
print('         GUESS THE NUMBER')
print('----------------------------------')

the_number = random.randint(0, 100) #randint is inclusive of both endpoints
guess = -1
name = input('Player, what is your name?')

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100:  ')
    guess = int(guess_text)
    if guess < the_number:
        print('Sorry {1}, your guess of {0} is too low.'.format(guess, name))
    elif guess > the_number:
        print('Sorry {1}, your guess of {0} is too high.'.format(guess, name))
    else:
        print('You win {1}! The number was {0}.'.format(guess, name))

