# #Opdracht 6 - Gemiddelde berekenen

#Manier 1
list2 = [22,45,45,3,7,88]
total_sum2 = sum(list2)/len(list2)
print(total_sum2)

#Manier 2
list1 = []
numbers = int(input("How many numbers in total: "))

for i in range(0,numbers):
    number = int(input())

    list1.append(number)

total_sum = sum(list1)/(len(list1))
print(total_sum)