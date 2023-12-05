'''Consider a tuple t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10), WAP to perform following operations:
a. Print half the values of the tuple in one line and the other half in the next line.
b. Print another tuple whose values are even numbers in the given tuple.
c. Concatenate a tuple t2=(11,13,15) with tl.
d. Return maximum and minimum value from this tuple'''


t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

print("half-half elements")
l=int(len(t1)/2)
for i in range(0,l):
    print(t1[i],end=" ")
print()  
for i in range(l,len(t1)):
    print(t1[i],end=" ")
print()

print("another tuple of even no. only")
tup=()
for i in t1:
    if i%2==0:
        t=(i,)
        tup=tup+t
print(tup)

print("concatenate tuple")
t2=(11,13,15)
tuple=t1+t2
print(tuple)

print("max and min no. from concatenate tuple")
print(max(tuple))
print(min(tuple))