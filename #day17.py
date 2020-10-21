########## learn some concept of array ###############


thisarray = ["shruti", "mohini","prachi", "karishma"]
while True:
    print("OPERATIONS ON THE LIST")
    print(" Enter 1 for printing Array")
    print(" Enter 2 for finding the length of the array")
    print(" Enter 3 for print the array in reverse order")
    print(" Enter 4 for change the value of the arraay")
    print(" Enter 5 for checking whether the item is present in the array or not")
    print(" Enter 6 for performing accessing task")
    choice= int(input(" Enter your choice : "))

    if choice == 1:
        print("Array is : ")
        for x in thisarray:
          print(x)
    elif choice == 2:
        print(" Length of the array is", len(thisarray))
    elif choice == 3:
        thisarray.reverse()
        print(" Reverse list is: ",thisarray)
        break
    elif choice == 4:
        index = int(input(" Enter the index value that you want to change the item value: "))
        changevalue = input("Enter change value: ")
        thisarray[index] = changevalue
        print(" NEW array IS ")
        for x in thisarray:
            print(x)
    elif choice == 5:
        item = input(" Enter the item that you want to check: ")
        if item in thisarray:
            print(" YES",item,"is persent in thisarray")

    elif choice == 6:
        print(" Enter 1 for access any index value of Array")
        print(" Enter 2 for starting till you want to print the Array")
        print(" Enter 3 from you want to print the Array till end of the Array")
        print(" Enter 4 for access a Array in range")
        print(" Enter 5 for accessing the last value of the Array")
        h = int(input(" Enter your choice : "))    
        if h == 1:
            index = int(input(" Enter the index value of that you want to access from the Array: "))
            print(thisarray[index])
        elif h == 2:
            end = int(input(" Enter the index value till you want to print the list: "))
            print(thisarray[:end+1])
        elif h == 3:
            start = int(input(" Enter the index value from you want to start acess: "))
            print(thisarray[start:])
        elif h == 4:
            start = int(input(" Enter the index value from you want to start acess: "))
            end = int(input(" Enter the index value till you want to print the list: "))
            print(thisarray[start:end+1])
        elif h == 5:
            print("The last value in list is: ",thisarray[-1])
        else:
            print("INVALID CHOICE")
    else:
        print("INVALID CHOICE")