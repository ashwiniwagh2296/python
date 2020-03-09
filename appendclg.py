import sys

clg_name="Modern college"
students = []
id_no = 1
while 1:
    print("[+] {} [+]".format(clg_name))
    print(" 1]add student \n 2] delete student \n")
    choise= int(input("enter your choice: "))
    if choise == 1:
        name = input("enter name: ")
        age = input("enter age: ")
        add = input("enter add: ")
        students.append([name,age ,add])
        print(students)