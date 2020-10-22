thisarray = ["shruti", "mohini","prachi", "karishma"]
while True:
    print("OPERATIONS ON THE LIST")
    print(" Enter 1 What is the difination of the array? ")
    print(" Enter 2 for printing Array")
    print(" Enter 3 for finding the length of the array")
    print(" Enter 4 for print the array in reverse order")
    print(" Enter 5 for change the value of the arraay")
    print(" Enter 6 for checking whether the item is present in the array or not")
    print(" Enter 7 for performing accessing task")
    print(" Enter 8 for performing adding and removing operations ")
    print(" Enter 9 for performing operations on two array")
    choice= int(input(" Enter your choice : "))
    print("*******************************************************")

    if choice == 1:
        print("Arrays are used to store multiple values in one single variable")
        print("Python does not have built-in support for Arrays, but Python Lists can be used instead.")
        print("This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the NumPy library.")
    elif choice == 2:
        print("Array is : ")
        for x in thisarray:
          print(x)
    elif choice == 3:
        print(" Length of the array is", len(thisarray))
    elif choice == 4:
        thisarray.reverse()
        print(" Reverse list is: ",thisarray)
        break
    elif choice == 5:
        index = int(input(" Enter the index value that you want to change the item value: "))
        changevalue = input("Enter change value: ")
        thisarray[index] = changevalue
        print(" NEW array IS ")
        for x in thisarray:
            print(x)
    elif choice == 6:
        item = input(" Enter the item that you want to check: ")
        if item in thisarray:
            print(" YES",item,"is persent in thisarray")

    elif choice == 7:
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
    elif choice == 8:
        print("  Enter 1 for performing adding task")
        print("  Enter 2 for performing removing task")
        ch = int(input("  Enter your choice: "))
        if ch == 1:
             print("   LET'S PERFORM SOME ADDING TASK ")
             print("    Enter 1 for add item from last in the present Array")
             print("    Enter 2 for adding item at which postion that want add in the present Array")
             i = int(input("    Enter your choice: "))
             if  i == 1:
                item = input("     Enter item that you want to add in the Array: ")
                thisarray.append(item)
                print("NOW LIST BECOME",thisarray)
             elif i == 2:
                item = input("     Enter item that you want to add in the Array: ")
                index = int(input("     Enter the position at you want to add the item in the Array: "))
                thisarray.insert(index,item)
                print("     NOW LIST BECOME",thisarray)
             else:
                print("INVALID CHOICE")
        elif ch == 2:
            print("    Enter 1 for removing particular item from the Array")
            print("    Enter 2 for removing last item from the Array")
            print("    Enter 3 for removing item from particular index value")
            print("    Enter 4 for removing whole Array")
            j = int(input("    Enter your choice: "))
            if j == 1:
                item = input("   Enter item that you want to remove from the present Array: ")
                thisarray.remove(item)
                print("     NOW ARRAY BECOME",thisarray)
            elif j == 2:
                thisarray.pop()
                print("     NOW ARRAY BECOME",thisarray)
            elif j == 3:
                index = int(input("     Enter the position at which you want to remove the item : "))
                del thisarray[index]
                print("     NOW ARRAY BECOME",thisarray)
            elif j == 4:
                thisarray.clear()
                print("     NOW ARRAY BECOME",thisarray)
            else:
                print("     INVALID CHOICE")

    elif choice == 9:
        print("  Enter 1 for adding two list")
        print("  Enter 2 for copy one array into another")
        k = int(input("  Enter your choice: "))
        if k == 1:
            print("   Array 1 is",thisarray)
            array2 =[]
            n = int(input("   How many item do you want to entered in the array 2? "))
            for x in range(n):
                item =input("   Enter item that you want to add in the array 2: ") #considering user will enter string 
                array2.append(item)
            print("   Array 2 is", array2)
            print("   Enter 1 if you want to add item in present Array?")
            print("   Enter 2 if you want to create another array which is the addition of present two array")
            l =int(input("   Enter your choice: "))

            if l == 1:
                #way 1
                for item in thisarray:   #Now list2 has list plus list 2 number as well"
                    array2.append(item)  # here we change the list 2 by adding list 1 item in them
                print(" After adding array 1 item in array 2 then array 2 become: ", array2)
                """
                #way 2
                array2.extend(thisarray)
                print(" After adding list 1 item in array 2 then array 2 become: ", array2)
                """
            elif l == 2:
                #way3
                addedarray = thisarray + array2 # this operation is used only add operator for adding two list, here we created list 3 which is addtion of list 1 and 2
                print("   After adding array2 in array1 array become", addedarray)
            else:
                print("INVALID CHOICE")    
        elif k == 2:
            copyarray = list(thisarray)
            print("Original Array is ", thisarray)
            print("Copy Array is ", copyarray)

    else:
        print("INVALID CHOICE")