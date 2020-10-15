############# proper maintain############
########## learn all concept of SET ###############


thisset1 = {34, 21, 56, 1, 7979, 45}
while True:
    print("MENU OF OPERATIONS")
    print(" Enter 1 for printing set")
    print(" Enter 2 for finding the length of the set")
    print(" Enter 3 for print the set in reverse order")
    print(" Enter 4 for change the value of the set")
    print(" Enter 5 for checking whether the item is present in the set or not")
    print(" Enter 6 for performing accessing task")
    print(" Enter 7 for performing adding and removing operations on set")
    print(" Enter 8 for performing operations on two set")
    e= int(input(" Enter your choice : "))
    
    if e == 1:
        print(" Set is : ",thisset1)
        """
        #way2
        for x in thisset1:
          print(x)
        """
    elif e == 2:
        print(" Length of the set is", len(thisset1))
    
    elif e == 3:
      print("Set are unordered and can not reverse" )
        
    elif e == 4:
        print("Once the set is created, we can not change its value but we can add and remove the values")
        
    elif e == 5:
        item = int(input(" Enter the item that you want to check: "))
        if item in thisset1:
            print(" YES",item,"is persent in given SET")
        else:
            print(" Not present in the given SET")
    elif e == 6:
        print(" You cannot access items in a set by referring to an index or a key.")
    
    elif e == 7:
        print("  Enter 1 for performing adding task")
        print("  Enter 2 for performing removing task")
                
        print("  ORIGINAL SET IS", thisset1)
        g = int(input("  Enter your choice: "))

        if g == 1:
            print("  Enter 1 if you want to add single item in the present set")
            print("  Enter 2 if you want to add multiple item in the present set")
            i = int(input("  Enter your choice: "))
            if  i == 1:
                item = int(input("  Enter item that you want to add in the set: "))
                thisset1.add(item)
                print(" NOW TUPLE BECOME",thisset1)
             
            elif i == 2:
                n = int(input("  How many  item do you want to add in the set : "))
                for x in range(n):
                    item = int(input("  Enter item that you want to add in the tuple: "))
                    thisset1.add(item)
                print("  NOW TUPLE BECOME",thisset1)
            else:
                print("INVALID CHOICE")
        elif g == 2:
            print("  Enter 1 for removing particular item from the tuple")
            print("  Enter 2 for clear the whole set")
            print("  Enter 3 for destroy the whole set")
            j = int(input("  Enter your choice: "))
            if j == 1:
                item = int(input(" Enter item that you want to remove from the present set : "))
                thisset1.remove(item)
                print("  NOW SET BECOME",thisset1)
            elif j == 2:
                thisset1.clear()
                print("  NOW SET BECOME",thisset1)
            elif j == 3:
                del thisset1
                print("  NOW SET BECOME",thisset1)  #it will raise an error like this set is not define
            else:
                print("  INVALID CHOICE")

    elif e == 8:
        print("  Enter 1 for adding two sets")
        print("  Enter 2 for copy one tuple into another")
        k = int(input("  Enter your choice: "))
        thisset2 = {12,115,19,48}
        print("   Set 1 is : ", thisset1)
        print("   Set 2 is", thisset2)
       
        if k == 1:
            print("   Enter 1 if you want to add set 2 in orginal set 1")
            print("   Enter 2 if you want to add set 1 in present set 2")
            print("   Enter 3 if you want to create new tuple which is the addition of present previous set ")
            j = int(input("   Enter your choice: "))
            if j == 1:
                thisset1.update(thisset2)
                print("  After adding set 1 item in set 2 then set 2 become: ", thisset1)
                print("  second set is : ",thisset2)
            elif j == 2:
                thisset2.update(thisset1)
                print("  After adding set 1 in set 2 then set 2 becomes: ", thisset2)  # here we change the set 2 by adding tuple 1 item in the set 2
                print("  first set is : ",thisset1)
            elif j == 3:
                addedset = thisset1.union(thisset2)     # union is used to create the third set
                print("  Our new set is ", addedset)
            else:
                print("  INVALID CHOICE")    
        elif k == 2:
            copyset = thisset1.copy()
            print("  Copy Set is ", copyset)
            
        
    else:
        print("INVALID CHOICE")

