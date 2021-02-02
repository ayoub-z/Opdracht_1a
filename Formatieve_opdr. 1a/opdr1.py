#Pyramid with for loops
def p_for():
    size = int(input("How many blocks high: "))
    if size == 0:
        print('No pyramid for you.')
    elif size < 0:
        print('Pyramid can\'t go underground!')
    else:
        for blocks in range(0,size+1):
            print (blocks * '*')
        for blocks in range(size-1, 0, -1):
            print (blocks * '*')

#Pyramid with while loops
def p_while():
    size = int(input("How many blocks high: "))
    blocks = 0
    while blocks < size:
        print(blocks * '*') 
        blocks += 1
    while blocks > 0:
        print(blocks * '*')
        blocks -= 1 

p_for()
