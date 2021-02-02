# ---Opdracht 2 - Tekstcheck
def tekst_check():
    userInput1 = input("Enter the first word or sentence: ")
    userInput2 = input("Enter the second word or sentence: ")

    counter = 0
    minimum = min(len(userInput1),len(userInput2))
    for i in range(0,minimum-1):
        while True:
            if userInput1[counter] != userInput2[counter]:
                print ('The first difference is on index: ',(counter+1))
                exit()
            elif counter == minimum-1:
                print ('There is no difference')
                exit()
            else:
                counter += 1

tekst_check()

