l=[]
n=int(input())
for _ in range(n):
    arr = input().strip().split(" ")
    choice = arr[0]
    if choice == "insert":
        l.insert(int(arr[1]),int(arr[2]))
    elif choice == "append":
        l.append(int(arr[1]))
    elif choice == "remove":
        l.remove(int(arr[1]))
    elif choice == "sort":
        l.sort()
    elif choice == "reverse":
        l.reverse()
    elif choice == "pop":
        l.pop()
    elif choice == "print":
        print(l)

