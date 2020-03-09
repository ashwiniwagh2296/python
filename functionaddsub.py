import sys
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
while 1:
    print("1] addition \n 2]substract \n")
    choise = int(input("Enter your choise: "))
    a = int(input("Enter your no :  "))
    b = int(input("Enter your no :  "))
    if choise == 1:
         c = add(a,b)
         print(c)
    elif choise ==2:
        c = sub(a,b)
        print(c)
    else:
        sys.exit()