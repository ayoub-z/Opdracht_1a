# ---Opdracht 3 - Lijstcheck

#(a)
def list_check():
    Numbers_list = [1,2,3,4,1,1.1]
    userInput = int(input('Which number would you like to check: '))

    if Numbers_list.count(userInput) == 0:
        print('The number', userInput, 'does not show up in the list.')
    else:
        print ('The number', userInput, 'shows up', Numbers_list.count(userInput), 'times in the list.')


#(b)
def list_diff():
    Numbers_list2 = [1,5,10,20,10,100,200,500,10]
    diff_list2 = []
    i = 0

    while i+1 < len(Numbers_list2):
        difference = (Numbers_list2[i+1] - Numbers_list2[i])
        diff_list2.append(difference)
        i += 1
    print('Difference between each two consecutive numbers in the list is as follows: ',diff_list2)


#(c)
def list_01():
    Numbers_list3 = [1,1,1,1,1,1,0,0,0,0,0,0,0]
    one = Numbers_list3.count(1)
    zero = Numbers_list3.count(0)

    if zero >= one:
        print('There are', zero, 'zeros, but only',one, 'ones. Remove',(zero+1)-one,'zeros.')
    elif one > 12:
        print('There are ', one, ' ones. That\'s ',one-12,' too many.')
    else:
        print('There are ',one, 'ones and ', zero, 'zeros. It works!')


list_check()
list_diff()
list_01()