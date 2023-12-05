"""WAP to perform the following operations on a string
a. Find the frequency of a character in a string.
b. Replace a character by another character in a string.
c. Remove the first occurrence of a character from a string.
d. Remove all occurrences of a character from a string."""
str=input("Enter a string:")
find=input("Enter any character from string:")
fre=str.count(find)
print("frequency of",find,"in string:",fre)
pre=input("Enter character to be replaced:")
new=input("Enter new character:")
str=str.replace(pre,new)
print(str)
rem=input("Enter character to be removed first occurence:")
str=str.replace(rem,'',1)
print(str)
delete= input("Enter character to be removed:")
f=str.count(delete)
str=str.replace(delete,'',f)    
print(str)