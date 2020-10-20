print("********** MENU***********")
print(" Enter 1 if you want to perform the task on function")
print(" Enter 2 if you  want to perform the task")
choice = int(input("Enter your choice: "))
if choice == 1:
    print(" Enter 1 for performing multiplication for dubling the number")
    print(" Enter 2 for performing multiplication for tripling the number")
    choice = int(input(" Enter your choice: "))
    if choice == 1:
        def myfun(n):
            return lambda a : a * n
        mydouble = myfun(2)
        print(mydouble(15))
    elif choice == 2:
        def myfun(n):
            return lambda a : a * n
        mytriple = myfun(3)
        print(mytriple(15))
    else:
        print(" INVALID CHOICE ")

elif choice == 2:
    print("Enter 1 for performing task with one arguement ")
    print("Enter 2 for performing task with two arguement ")
    print("Enter 3 for performing task with three arguement ")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        x = lambda a: a + 10
        print(x(7))
    elif choice == 2:
        x = lambda a , b:a*b
        print(x(3,4))
    elif choice == 3:
        x = lambda a,b,c: a+b+c
        print(x(10,20,30))
    else :
        print(" INVALID CHOICE ")
else :
        print(" INVALID CHOICE ")
