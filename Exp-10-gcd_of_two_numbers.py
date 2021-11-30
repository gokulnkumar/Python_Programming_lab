a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
n1=a
n2=b
while b:
    c=b
    b=a%b
    a=c
print("gcd of",n1,"and",n2,"is",a)

