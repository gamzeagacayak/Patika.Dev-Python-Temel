"""
Task: Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hast(t).

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported
"""
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    
for i in range(len(integer_list)):
   integer_list[i] = int(integer_list[i])
T = tuple(integer_list)
print hash(T)
