print("********** MENU***********")
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