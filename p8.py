'''WAP to create a list of the cubes of only the even integers appearing in the 
input list (may have elements of other types also) using the following:
a. 'for' loop
b. list comprehension'''


L=[]
choice=int(input("Enter 1 to add element:"))
while choice==1:
    ele=(input("Enter element:" ))
    L.insert(len(L),ele)
    choice=int(input("Enter 1 to add more elements oterwise 0:"))
print("list=",L)
cube=[]
for i in L:
    if i.isdigit():
        if int(i)%2==0:
            n=int(i)**3
            cube.insert(len(cube),n)
    elif i[0]=='-':
        j=i[1:]
        if j.isdigit():
            if int(j)%2==0:
                n=-int(j)**3
                cube.insert(len(cube),n)       
print(cube)
