# learn list

thislist = [1,2,3,45,56,67,23,44,56]
while True:
    print("MENU")
    print(" Enter choice 1 for printing list")
    print(" Enter choice 2 for accesS any index value of list")
    print(" Enter choice 3 for access a list in range")
    choice= int(input("Enter your choice :"))
    if choice == 1:
        print("list is : ")
        for x in thislist:
          print(x)
    elif choice == 2:
        index = int(input(" Enter the index value of that you want to access from the list: "))
        print(thislist[index])
    elif choice == 3:
        start = int(input(" Enter the index value from you want to start acess: "))
        end = int(input(" Enter the index value till you want to print the list: "))
        print(thislist[start:end+1])

    else:
        print("INVALID CHOICE")
