a = int(input("Enter your no of a: "))
b = int(input("Enter your no of b: "))
try:
    c= a/b
    print("{}".format(c))
except:
    print ("Out of range")
finally:
    print("Ashu wagh")
