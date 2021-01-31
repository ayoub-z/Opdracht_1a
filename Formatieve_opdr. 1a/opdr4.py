#Opdracht 4 - Palindroom

#Manier 1
userInput = input('Woord: ')
a = userInput
b = userInput[::-1]

if a == b:
    print('Word is a palindrome!')
else:
    print('Word is not a palindrome')

#Manier 2
def palindrome(i):
    if i == i[::-1]:
        print('Word is a palindrome!')
    else:
        print('Word is not a palindrome')

palindrome('jaj')


