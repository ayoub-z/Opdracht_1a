import string
import collections

rotate_string = input('Geef een tekst: ')
n = int(input('Geef een rotatie: '))

def caesar(rotate_string, n):


    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    upper.rotate(n)
    lower.rotate(n)

    upper = ''.join(list(upper))
    lower = ''.join(list(lower))

    return rotate_string.translate(str.maketrans(string.ascii_uppercase, upper))\
        .translate(str.maketrans(string.ascii_lowercase, lower))

print(caesar(rotate_string,n))