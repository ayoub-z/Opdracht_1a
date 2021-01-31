# ---Opdracht 3 - Lijstcheck


#(a)
numbers = [1,2,3,4,1,1.1]
userInput = int(input('Welk getal: '))
x = numbers.count(userInput)

print(x)


#(b)
lijst = [1,5,10,20,10,100,200,500,10]
diff = lijst[1] - lijst[0]
counter = 0

while counter+1 < len(lijst):
    print (lijst[counter+1] - lijst[counter], end = ', ')
    counter += 1


#(c)
numbers1 = [1,1,1,1,1,1,0,0,0,0,0,0,0]
one = numbers1.count(1)
zero = numbers1.count(0)

if zero >= one:
    print('There are', zero, 'zeros, but only',one, 'ones. Remove',(zero+1)-one,'zeros.')
elif one > 12:
    print('There are ', one, ' ones. That\'s ',one-12,' too many.')
else:
    print('There are ',one, 'ones and ', zero, 'zeros. It works!')