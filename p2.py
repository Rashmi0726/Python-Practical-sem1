"""WAP to accept a number 'n' and
a. Check if 'n' is prime
h. Generate all prime numbers till 'n'
e. Generate first 'n' prime numbers
d. This program may be done using functions."""
n=int(input("Enter a positive number:"))
if n<=0:
    print(n,"is not a prime no.")
else:
    for i in range(2,n):
        if n%i==0:
            print(n,"is not a prime no.")
            break
    else:
        print(n,"is a prime no.")
    print("prime no. till",n)
    for x in range(2,n): 
        for y in range(2,x):
            if x%y==0:
                break
        else:
            print(x)    
    print("first",n,"prime no.")
    a=0
    x=2
    while a<n:
        for i in range(2,x):
            if x%i==0:
                break
        else:
            print(x)
            a+=1
        x+=1
      