#WAP to create a pyramid of the character'*' and a reverse pyramid
r= 5
print("*pyramid pattern")
for i in range(r):
    for j in range(r-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()

    
print("*reverse pyramid pattern")
for i in range(r):
    for j in range(i):
        print(" ",end="")
    for j in range(2*(r-i)-1):
        print("*",end="")
    print()

