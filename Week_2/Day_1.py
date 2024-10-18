    # Simple square star pattern 


# n = int(input("Enter number: "))

"""
for i in range(n):
    for j in range(n):
        print("$", end=' ')
    print() 
"""


    # printing incresing triangle pattern

"""
n = int(input("Enter number: "))

for i in range(n):
    for j in range(i+1):
        print("*", end=' ')
    print()
"""

    # Printing Decreasing triangle pattern 

"""
n = int(input("Enter number: "))

for i in range(n):
    for j in range(i,n):
        print("*", end=' ')
    print()
"""


    # Printing Right side Triangle

"""
n = int(input("Enter number: "))

for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i+1):
        print("*",end=' ')
    print()
"""


    # Printing hill/pyramid pattern 

"""
n = int(input("Enter number: "))

for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
"""


        # Printing rerverse Hill/pyramid pattern

"""
n = int(input("Enter number: "))

for i in range(n):
    for j in range(i+1):
        print(' ', end=' ')
    for j in range(i,n-1):
        print("*",end=' ')
    for j in range(i,n):
        print("*", end=' ')
    print()
"""


    # Printing Diamond pattern

n = int(input("Enter number: "))

for i in range(n-1):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n-1):
        print('*',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    print()






