for i in range(1,6):
    for x in range(5-i):
        print(" ",end="")
    for n in range(1,i+1):
        print("*",end="")
    for y in range(0,i-1):
        print("*",end="")
    print()