# creating = True

# while creating:
#     size = int(input("Hoe groot: "))
#     if size == 0:
#         creating = False
#         print('No pyramid for you.')
#     else:
#         for blocks in range(1,size+1):
#             print (blocks * '*')
#         for blocks in range(size-1, 0, -1):
#             print (blocks * '*')
#             creating = False




# # ---Opdracht 1 - Pyramide

# size = int(input("Hoe groot: "))

# if size == 0:
#     print('No pyramid for you.')
# for blocks in range(1,size+1):
#     print (blocks * '*')
# for blocks in range(size-1, 0, -1):
#     print (blocks * '*')
#     creating = False




# # Failed test
# userInput = int(input("Amount of rows: "))
# row = 0

# while (row < userInput):
#     row += 1
#     spaces = userInput - row




# # ---Opdracht 2 - Tekstcheck

# userInput1 = input("Geef een string: ")
# userInput2 = input("Geef een string: ")

# counter = 0
# minimum = min(len(userInput1),len(userInput2))
# running = True

# for i in range(0,minimum-1):
#     while running:
#         if userInput1[counter] != userInput2[counter]:
#             print ('Het eerste verschil zit op index: ',(counter+1))
#             running = False
#         elif counter == minimum-1:
#             print ('Het eerste verschil zit op indexx: ', (counter +2))
#             running = False
#         else:
#             counter += 1



# # ---Opdracht 3 - Lijstcheck


# #(a)
# numbers = [1,2,3,4,1,1.1]
# userInput = int(input('Welk getal: '))
# x = numbers.count(userInput)

# print(x)


# #(b)
# lijst = [1,5,10,20,10,100,200,500,10]
# diff = lijst[1] - lijst[0]
# counter = 0

# while counter+1 < len(lijst):
#     print (lijst[counter+1] - lijst[counter], end = ', ')
#     counter += 1

# #better method on StackOverflow
# print [ y - x for x, y in zip(lijst[:-1],lijst[1:])]


# #(c)
# numbers1 = [1,1,1,1,1,1,0,0,0,0,0,0,0]
# one = numbers1.count(1)
# zero = numbers1.count(0)

# if zero >= one:
#     print('There are', zero, 'zeros, but only',one, 'ones. Remove',(zero+1)-one,'zeros.')
# elif one > 12:
#     print('There are ', one, ' ones. That\'s ',one-12,' too many.')
# else:
#     print('There are ',one, 'ones and ', zero, 'zeros. It works!')



# #Opdracht 4 - Palindroom

# #Manier 1
# userInput = input('Woord: ')
# a = userInput
# b = userInput[::-1]

# if a == b:
#     print('Word is a palindrome!')
# else:
#     print('Word is not a palindrome')

# #Manier 2
# def palindroom(i):
#     if i == i[::-1]:
#         print('Word is a palindrome!')
#     else:
#         print('Word is not a palindrome')

# # palindroom('jaj')


# #Opdracht 5 - Sorteren

# lijst_getallen = [9, 22, 19, 3, 7]
# lijst_getallen.sort()
# print(lijst_getallen)
