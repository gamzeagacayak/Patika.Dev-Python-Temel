"""
Task: Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
"""

def is_leap(year):
    leap = False
    
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
    
    return leap

year = int(input())
print(is_leap(year))
