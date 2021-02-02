# #Opdracht 6 - Gemiddelde berekenen

#Manier 1
def sum1():
    list2 = [22,45,45,3,7,88]
    total_sum2 = sum(list2)/len(list2)
    print('The sum is:',total_sum2)

#Manier 2
def sum2():
    list1 = []
    numbers = int(input("How many numbers would you like to enter: "))
    for i in range(0,numbers):
        number = int(input('Please enter the numbers one by one: '))
        list1.append(number)

    total_sum = sum(list1)/(len(list1))
    print('The sum is:',total_sum)

sum1()