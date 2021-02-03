#Opdracht 4 - Palindroom

#Manier 1
def palindrome():
    userInput = input('Enter word: ')
    a = userInput
    b = userInput[::-1]

    if a == b:
        print('The word',a, 'is a palindrome!')
    else:   
        print('The word',a, 'is not a palindrome.')

#Manier 2
def palindrome2(i):
    if i == i[::-1]:
        print('The word',i, 'is a palindrome!')
    else:
        print('The word',i, 'is not a palindrome.')

palindrome()
palindrome2('lepel')
palindrome2('fiets')