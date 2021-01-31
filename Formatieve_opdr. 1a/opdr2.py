# ---Opdracht 2 - Tekstcheck

userInput1 = input("Geef een string: ")
userInput2 = input("Geef een string: ")

counter = 0
minimum = min(len(userInput1),len(userInput2))
running = True

for i in range(0,minimum-1):
    while running:
        if userInput1[counter] != userInput2[counter]:
            print ('Het eerste verschil zit op index: ',(counter+1))
            running = False
        elif counter == minimum-1:
            print ('Het eerste verschil zit op indexx: ', (counter +2))
            running = False
        else:
            counter += 1



