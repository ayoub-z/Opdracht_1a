def FizzBuzz():
    for i in range (1,101):
        x = (i % 3 == 0)
        q = (i % 5 == 0)
        if x == True:
            if (x and q) == True:
                print('fizzbuzz')
            else:
                print('fizz')
        elif q == True:
            if (x and q) == True:
                print('fizzbuzz')
            else:
                print('buzz')
        else:
            print(i)

FizzBuzz()            