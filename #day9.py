
########## learn some concept of set ###############


thisset1 = {34, 21, 56, 1, 7979, 45}
while True:
    print("MENU OF OPERATIONS")
    print(" Enter 1 for printing set")
    print(" Enter 2 for finding the length of the set")
    print(" Enter 3 for print the set in reverse order")
    print(" Enter 4 for change the value of the set")
    print(" Enter 5 for checking whether the item is present in the set or not")
    print(" Enter 6 for performing accessing task")
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
        print(" Once the set is created, we can not change its value but we can add and remove the values")
        
    elif e == 5:
        item = int(input(" Enter the item that you want to check: "))
        if item in thisset1:
            print(" yes",item,"is persent in given set")
        else:
            print(" Entered item is not present in the given set")
    elif e == 6:
        print(" Set is uni-index, so  you cannot access items in a set by referring to an position.")
    
    else:
        print("INVALID CHOICE")

