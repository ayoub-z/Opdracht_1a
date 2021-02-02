from random import *

def random1():
    number = randrange(1,6)
    while True:
        guess = int(input('The number is between 1 and 5. Enter your guess or type 0 to stop: '))
        if guess == number:
            print('Good job, you got it!')
            break
        elif guess == 0:
            print('Ending guessing session..')
            break
        elif guess > number:
            print('Your guess is too high. Try again..')
        else:
            print('Your guess is too low. Try again..')

random1()
