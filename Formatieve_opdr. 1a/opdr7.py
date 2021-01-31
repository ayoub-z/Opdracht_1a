from random import *


# --Short version
number = randrange(1,6)
while True:
    guess = int(input('Guess the number: '))
    if guess == number:
        print('Good job, you got it!')
        break
    else:
        print('Sorry, wrong guess. Try again..')
        pass


# # --Longer version
# end = int(input('How high can the number go: '))

# number = randrange(1, int(end+1))
# yes = ['Yes', 'yes', 'Y', 'y']
# no = ['No', 'no', 'N', 'n']

# while True:
#     guess = int(input('Guess the number: '))
#     if guess == number:
#         print('Good job, you got it!')
#         break
#     elif guess > number:
#         print('Your guess is too high..')
#         userinput = input('Would you like to guess again? y/n: ')
#         if userinput in yes:
#             print('Continuing..')
#             pass
#         elif userinput in no:
#             print('Ending guessing session..')
#             break
#         else:
#             print('Invalid input, ending guessing session...')
#             break
#     else:
#         print('Your guess is too low..')
#         userinput = input('Would you like to guess again? y/n: ')
#         if userinput in yes:
#             print('Continuing..')
#             pass
#         elif userinput in no:
#             print('Ending guessing session..')
#             break
#         else:
#             print('Invalid input, ending guessing session..')
#             break

