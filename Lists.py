"""
Task: Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. 
Iterate through each command in order and perform the corresponding operation on your list.
"""
if __name__ == '__main__':
    N = int(input())
    s = []
    l = []

    for i in range(N):
        x = input().split()
        s.append(x)

    for i in range(len(s)):
        if s[i][0] == 'insert':
            x = int(s[i][1])
            y = int(s[i][2])
            l.insert(x,y)
        elif s[i][0] == 'print':
            print(l)
        elif s[i][0] == 'remove':
            l.remove(int(s[i][1]))
        elif s[i][0] == 'append':
            l.append(int(s[i][1]))
        elif s[i][0] == 'sort':
            l.sort()
        elif s[i][0] == 'pop':
            l.pop()
        elif s[i][0] == 'reverse':
            l.reverse()
