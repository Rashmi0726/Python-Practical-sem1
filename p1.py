#WAP to solve roots of a quadratic equation
#Quadratic Equation=ax^2 + bx + c
a=int(input("value of a:"))
b=int(input("value of b:"))
c=int(input("value of c:"))
D=(b**2)-4*(a*c)
print("discriminant=",D)
if D<0:
    print("No Real Roots Exist")
elif D==0:
    x=((-b)+(D**0.5))/(2*a)
    print("Same Roots Exist:",x)
else:
    x1=((-b)+(D**0.5))/(2*a)
    x2=((-b)-(D**0.5))/(2*a)
    print("Roots:",x1,"and",x2)