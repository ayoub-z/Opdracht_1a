size = int(input("How many blocks high: "))

if size == 0:
    print('No pyramid for you.')
elif size < 0:
    print('Pyramid can\'t go underground!')
else:
    for blocks in range(0,size):
        print (blocks * '*')
    for blocks in range(size-1, 0, -1):
        print (blocks * '*')
        creating = False
