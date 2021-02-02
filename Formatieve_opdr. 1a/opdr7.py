from random import *


# --Short version
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



# # --Longer version
def random2():
    end = int(input('How high do you wanna guess: '))

    number = randrange(1, int(end+1))
    yes = ['Yes', 'yes', 'Y', 'y']
    no = ['No', 'no', 'N', 'n']

    while True:
        guess = int(input('Guess the number: '))
        if guess == number:
            print('Good job, you got it!')
            break
        elif guess > number:
            print('Your guess is too high..')
            userinput = input('Would you like to guess again? y/n: ')
            if userinput in yes:
                print('Continuing..')
                pass
            elif userinput in no:
                print('Ending guessing session..')
                break
            else:
                print('Invalid input, ending guessing session...')
                break
        else:
            print('Your guess is too low..')
            userinput = input('Would you like to guess again? y/n: ')
            if userinput in yes:
                print('Continuing..')
                pass
            elif userinput in no:
                print('Ending guessing session..')
                break
            else:
                print('Invalid input, ending guessing session..')
                break

random1()