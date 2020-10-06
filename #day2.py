#******* printing number******


while True:
    print("MENU")
    print(" Enter choice 1 for printing natural number")
    print(" Enter choice 2 for printing whole number")
    print(" Enter choice 3 for printing odd number")
    print(" Enter choice 4 for printing even number")
    print(" Enter choice 5 for printing prime number")
    choice= int(input("Enter your choice :"))
    lower = int(input("Enter the lower number from you want to print the number: "))
    upper = int(input("Enter the upper number till you want to print the number: "))

    if choice == 1:
        print("NATURAL NUMBER ARE:")
        for x in range(lower, upper+1):
            print(x)

    elif choice == 2:
        print("WHOLE NUMBER ARE:")
        for x in range(lower,upper+1):
            print(x)

    elif choice == 3:
        print("ODD NUMBER ARE:")
        for x in range(lower, upper+1,2):
            print(x)
    
    elif choice == 4:
        print("EVEN NUMBER ARE:")
        for x in range(2, upper+1,2):
            print(x)

    elif choice == 5:
        print("PRIME NUMBER ARE:")
        for num in range(lower, upper+1):
            if( num>1):                     # prime number is started from 2 so, every prime number must be greater than one
                for i in range(2,num):
                    if (num%i)== 0:
                        break               # if number is divisible by previous number than it is not a prime nummber so,
                                            #for that we will move to next number for finding it is prime or not
                else:
                    print(num)

    else :
        print("INVALID CHOICE")
        


