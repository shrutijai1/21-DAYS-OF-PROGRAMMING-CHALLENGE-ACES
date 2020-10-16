n = int(input())
input_list = input().strip().split() #list of string
for x in range(n): 
    input_list[x] = int(input_list[x])  #convert list of string into integer string

input_tuple = tuple(input_list) #converting list into tuple
print(hash(input_tuple))

"""
Note that:
swapcase() function is used to convert uppercase letter into lower case of the string and vice versa
and we use strip its because if a user input 09 its means 9 na, so we need to remove 0 from 09 thats why we use strip
and we use split function for taking multiple input at a time
"""
