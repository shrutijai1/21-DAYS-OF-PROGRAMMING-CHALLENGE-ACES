########## learn all concept of Tuple ###############


thistuple1 = (1,2,3,45,56)
while True:
    print("OPERATIONS ON THE LIST")
    print(" Enter 1 for printing tuple")
    print(" Enter 2 for finding the length of the tuple")
    print(" Enter 3 for print the tuple in reverse order")
    print(" Enter 4 for change the value of the tuple")
    print(" Enter 5 for checking whether the item is present in the tuple or not")
    print(" Enter 6 for performing accessing task")
    print(" Enter 7 for performing adding and removing operations on tuple")
    print(" Enter 8 for performing operations on two tuple")
    e= int(input(" Enter your choice : "))
    
    if e == 1:
        print(" Tuple is : ",thistuple1)
        """
        #way2
        for x in thistuple:
          print(x)
        """
    elif e == 2:
        print(" Lenght of the tuple is", len(thistuple1))
    elif e == 3:
        x = reversed(thistuple1)
        thistuple1 = tuple(x)
        print(" Reverse tuple is: ",thistuple1)
    elif e == 4:
        thislist1 = list(thistuple1)
        position = int(input(" Enter the position that you want to change the item value: "))
        changevalue = int(input(" Enter change value: "))
        index = position -1
        thislist1[index] = changevalue
        thistuple1 = tuple(thislist1)
        print(" NEW TUPLE IS ",thistuple1)
        """
        for x in thislist:
            print(x)
        """
    elif e == 5:
        item = int(input(" Enter the item that you want to check: "))
        if item in thistuple1:
            print(" YES",item,"is persent in given Tuple")
        else:
            print(" Not present in the given tuple")
    elif e == 6:
        print(" Enter 1 for access any index value of Tuple")
        print(" Enter 2 for starting till you want to print the Tuple")
        print(" Enter 3 from you want to print the item till end of the Tuple")
        print(" Enter 4 for access a Tuple in range")
        print(" Enter 5 for accessing the last value of the Tuple")
        print(" Original Tuple is : ",thistuple1)
        h = int(input(" Enter your choice : "))    
        if h == 1:
            index = int(input(" Enter the position of that you want to access from the Tuple: "))
            print(" value is:",thistuple1[index-1])
        elif h == 2:
            end = int(input(" Enter the position till you want to print the Tuple: "))
            print(thistuple1[:end])
        elif h == 3:
            start = int(input(" Enter the position from you want to start acess: "))
            print(thistuple1[start-1:])
        elif h == 4:
            start = int(input(" Enter the position from you want to start acess: "))
            end = int(input(" Enter the position till you want to print the Tuple: "))
            print(thistuple1[start-1:end])
        elif h == 5:
            print("The last value in the tuple is: ",thistuple1[-1])
        else:
            print("INVALID CHOICE")
    
    
    elif e == 7:
        """
        NOTE:
        A tuple is a collection which is ordered and unchangeable,
        We can not add and remove the item in tuple directly, so for these operations first we need to convert first tuple into list then
        perform operations and again convert list into tuple
        """
        print("  Enter 1 for performing adding task")
        print("  Enter 2 for performing removing task")
        print("  ORIGINAL TUPLE IS", thistuple1)
        g = int(input("  Enter your choice: "))
        if g == 1:
             
             print("  Enter 1 for add item from last in the present list")
             print("  Enter 2 for adding item at which postion that want add in the present list")
             i = int(input("  Enter your choice: "))
             if  i == 1:
                item = int(input("  Enter item that you want to add in the tuple: "))
                thislist1 = list(thistuple1)
                thislist1[-1] = item
                thistuple1 = tuple(thislist1)
                print(" NOW TUPLE BECOME",thistuple1)
             elif i == 2:
                item = int(input("  Enter item that you want to add in the tuple: "))
                position = int(input("  Enter the position at you want to add the item in the tuple: "))
                thislist1 = list(thistuple1)
                indexvalue = position - 1
                thislist1[indexvalue] = item
                thistuple1 = tuple(thislist1)
                print("  NOW TUPLE BECOME",thistuple1)
             else:
                print("INVALID CHOICE")
        elif g == 2:
            print("  Enter 1 for removing particular item from the tuple")
            print("  Enter 2 for removing last item from the tuple")
            print("  Enter 3 for removing item from particular position from the tuple")
            print("  Enter 4 for removing whole tuple")
            j = int(input("  Enter your choice: "))
            if j == 1:
                item = int(input(" Enter item that you want to remove from the present list: "))
                thislist1 = list(thistuple1)
                thislist1.remove(item)
                thistuple1 = tuple(thislist1)
                print("  NOW LIST BECOME",thistuple1)
            elif j == 2:
                thislist1 = list(thistuple1)
                thislist1.pop()
                thistuple1 = tuple(thislist1)
                print("  NOW LIST BECOME",thistuple1)
            elif j == 3:
                position = int(input("  Enter the position at which you want to remove the item : "))
                thislist1 = list(thistuple1)
                indexvalue = position - 1
                del thislist1[indexvalue] 
                thistuple1 = tuple(thislist1)
                print("  NOW TUPLE BECOME",thistuple1)
            elif j == 4:
                thislist1 = list(thistuple1)
                thislist1.clear()
                thistuple1 = tuple(thislist1)
                print("  NOW TUPLE BECOME",thistuple1)
            else:
                print("  INVALID CHOICE")

    elif e == 8:
        
        print("  Enter 1 for adding two tuple")
        print("  Enter 2 for copy one tuple into another")
        k = int(input("  Enter your choice: "))
        n = int(input("  How many item do you want to entered in the tuple 2? "))
        thislist1 = []
        for x in range(n):
            item =input("   Enter item that you want to add in the Tuple 2: ")                             #considering user will enter string 
            thislist1.append(item)
        thistuple2 = tuple(thislist1)
        print("   Tuple 2 is", thistuple2)
        print("   ORIGINAL TUPLE IS: ", thistuple1)
        
       
        if k == 1:
            print("   Enter 1 if you want to add tuple2 in orginal Tuple1")
            print("   Enter 2 if you want to add tuple1 in present Tuple2")
            print("   Enter 3 if you want to create new tuple which is the addition of present previous tuple")
            j = int(input("   Enter your choice: "))
            if j == 1:
                thistuple1 = thistuple1 + thistuple2
                print("  After adding tuple 1 item in tuple 2 then tuple 2 become: ", thistuple1)
            elif j == 2:
                thistuple2 = thistuple2 + thistuple1
                print("  After adding tuple 1 in tuple 2 then tuple 2 becomes: ", thistuple2) # here we change the tuple 2 by adding tuple 1 item in the tuple 2
               
            elif j == 3:
                addedtuple = thistuple1 + thistuple2     # this operation is used only add operator for adding two tuple, here we created list 3 which is addtion of tuple 1 and 2
                print("  our new tuple is ", addedtuple)
            else:
                print("  INVALID CHOICE")    
        elif k == 2:
            thislist1 = list(thistuple1)
            copylist = thislist1.copy()
            copytuple = tuple(copylist)
            print("  Copy list is ", copytuple)
            
        
    else:
        print("INVALID CHOICE")

