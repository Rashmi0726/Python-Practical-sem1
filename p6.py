#WAP to swap the first n characters of two strings
str1=input("Enter first string:")
str2=input("Enter second string:")
n=int(input("Enter total no. of characters to be swap:"))
str3=str1[:n]
str4=str2[:n]
str1=str1.replace(str3,str4)
str2=str2.replace(str4,str3)
print(str1)
print(str2)
