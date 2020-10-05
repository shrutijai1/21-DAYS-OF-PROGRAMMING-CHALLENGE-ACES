#************** CALCULATOR**************

def ad(a,b):
    c = a+b
    print("Addition of two number is ",c)

def sub(a,b):
    c = a-b
    print("Subtraction of two number is ",c)

def mul(a,b):
    c = a*b
    print("Multiplication of two number is ",c)

def div(a,b):
    c = a/b
    print("Division of two number is ",c)

def mod(a,b):
    c = a%b
    print("Modulation of two number is ",c)





while True:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("MENU")
    print(" Enter 1 for addition of two number: ")
    print(" Enter 2 for subraction of two number: ")
    print(" Enter 3 for multiplication of two number: ")
    print(" Enter 4 for division of two number: ")
    print(" Enter 5 for modulas of two number: ")
    choice = int(input(" enter your choice from menu: "))

    if choice == 1:
        ad(a,b)
        #print(add)
        break
    elif choice == 2:
        sub(a,b)
        break
       # print(sb)
    elif choice == 3:
         mul(a,b)
         break
    elif choice == 4:
        div(a,b)
        break
    elif choice == 5:
        mod(a,b)
        break
    else:
        print("INVALID CHOICE")
        


