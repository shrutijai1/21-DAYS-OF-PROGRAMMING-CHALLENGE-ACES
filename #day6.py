########## learn all concept of list ###############


thislist = [1,2,3,45,56,67,23,44,56]
while True:
    print("OPERATIONS ON THE LIST")
    print(" Enter 1 for printing list")
    print(" Enter 2 for finding the length of the list")
    print(" Enter 3 for print the list in reverse order")
    print(" Enter 4 for change the value of the list")
    print(" Enter 5 for checking whether the item is present in the list or not")
    print(" Enter 6 for performing accessing task")
    print(" Enter 7 for performing adding and removing operations ")
    print(" Enter 8 for performing operations on two list")
    choice= int(input(" Enter your choice : "))
    
    if choice == 1:
        print("list is : ")
        for x in thislist:
          print(x)
    elif choice == 2:
        print(" Lenght of the list is", len(thislist))
    elif choice == 3:
        thislist.reverse()
        print(" Reverse list is: ",thislist)
        break
    elif choice == 4:
        index = int(input(" Enter the index value that you want to change the item value: "))
        changevalue = int(input("Enter change value: "))
        thislist[index] = changevalue
        print(" NEW LIST IS ")
        for x in thislist:
            print(x)
    elif choice == 5:
        item = int(input(" Enter the item that you want to check: "))
        if item in thislist:
            print(" YES",item,"is persent in thislist")
    
    elif choice == 6:
        print(" Enter 1 for access any index value of list")
        print(" Enter 2 for starting till you want to print the list")
        print(" Enter 3 from you want to print the list till end of the list")
        print(" Enter 4 for access a list in range")
        print(" Enter 5 for accessing the last value of the list")
        h = int(input(" Enter your choice : "))    
        if h == 1:
            index = int(input(" Enter the index value of that you want to access from the list: "))
            print(thislist[index])
        elif h == 2:
            end = int(input(" Enter the index value till you want to print the list: "))
            print(thislist[:end+1])
        elif h == 3:
            start = int(input(" Enter the index value from you want to start acess: "))
            print(thislist[start:])
        elif h == 4:
            start = int(input(" Enter the index value from you want to start acess: "))
            end = int(input(" Enter the index value till you want to print the list: "))
            print(thislist[start:end+1])
        elif h == 5:
            print("The last value in list is: ",thislist[-1])
        else:
            print("INVALID CHOICE")
    
    
    elif choice == 7:
        print("  Enter 1 for performing adding task")
        print("  Enter 2 for performing removing task")
        ch = int(input("  Enter your choice: "))
        if ch == 1:
             print("   LET'S PERFORM SOME ADDING TASK ")
             print("    Enter 1 for add item from last in the present list")
             print("    Enter 2 for adding item at which postion that want add in the present list")
             i = int(input("    Enter your choice: "))
             if  i == 1:
                item = int(input("     Enter item that you want to add in the list: "))
                thislist.append(item)
                print("NOW LIST BECOME",thislist)
             elif i == 2:
                item = int(input("     Enter item that you want to add in the list: "))
                index = int(input("     Enter the position at you want to add the item in the list: "))
                thislist.insert(index,item)
                print("     NOW LIST BECOME",thislist)
             else:
                print("INVALID CHOICE")
        elif ch == 2:
            print("    Enter 1 for removing particular item from the list")
            print("    Enter 2 for removing last item from the list")
            print("    Enter 3 for removing item from particular index value")
            print("    Enter 4 for removing whole list")
            j = int(input("    Enter your choice: "))
            if j == 1:
                item = int(input("   Enter item that you want to remove from the present list: "))
                thislist.remove(item)
                print("     NOW LIST BECOME",thislist)
            elif j == 2:
                thislist.pop()
                print("     NOW LIST BECOME",thislist)
            elif j == 3:
                index = int(input("     Enter the position at which you want to remove the item : "))
                del thislist[index]
                print("     NOW LIST BECOME",thislist)
            elif j == 4:
                thislist.clear()
                print("     NOW LIST BECOME",thislist)
            else:
                print("     INVALID CHOICE")

    elif choice == 8:
        print("  Enter 1 for adding two list")
        print("  Enter 2 for copy one list into another")
        k = int(input("  Enter your choice: "))
        if k == 1:
            print("   list 1 is",thislist)
            list2 =[]
            n = int(input("   How many item do you want to entered in the list 2? "))
            for x in range(n):
                item =input("   Enter item that you want to add in the list2: ") #considering user will enter string 
                list2.append(item)
            print("   list 2 is", list2)
            print("   Enter 1 if you want to add item in present list?")
            print("   Enter 2 if you want to create another list which is the addition of present two list")
            l =int(input("   Enter your choice: "))

            if l == 1:
                #way 1
                for item in thislist:   #Now list2 has list plus list 2 number as well"
                    list2.append(item)  # here we change the list 2 by adding list 1 item in them
                print(" After adding list 1 item in list2 then list 2 become: ", list2)
                """
                #way 2
                list2.extend(thislist)
                print(" After adding list 1 item in list2 then list 2 become: ", list2)
                """
            elif l == 2:
                #way3
                addedlist = thislist + list2 # this operation is used only add operator for adding two list, here we created list 3 which is addtion of list 1 and 2
                print("   After adding list2 in list1 list become", addedlist)
            else:
                print("INVALID CHOICE")    
        elif k == 2:
            copylist = list(thislist)
            print("Original list is ", thislist)
            print("copy list is ", copylist)
            
        
    else:
        print("INVALID CHOICE")

"""
n = int(input("  no of value do you  want to entered"))
list2 = []
for x in range(n+1):
    item = input(" Enter your item value")
    l.append(item)
print(l)
"""

