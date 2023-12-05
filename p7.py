'''Write a function that accepts two strings and returns the indices of
all the occurrences of the second string in the first string as a list.
If the second string is not present in the first string then it should return -1'''

def func(str1,str2):
    list=[]
    for i in str2:
        if i in str1:
            n=str2.index(i)
            list.insert(len(list),n)    
    if list==[]:
        print("-1")
    else:
        print(list)

str1=input("Enter 1st sting:")
str2=input("Enter 2nd string:")
func(str1,str2)