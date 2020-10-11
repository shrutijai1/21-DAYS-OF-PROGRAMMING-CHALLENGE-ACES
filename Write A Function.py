# Way 1 (use single line if else)

def is_leap(year):
    leap = False
    if year%400 == 0:
        leap = True
    elif year%4 == 0 and year%100 != 0:
        leap = True
    else:
        leap = False
    
    return leap

"""
# use single line if else
def is_leap(year):
    leap=False
    leap= "True" if year%400==0 else "True" if year%100 != 0 and year%4 == 0 else "False"
    return leap
year = int(raw_input())
print is_leap(year)
"""
#Note: you can use any one way 
