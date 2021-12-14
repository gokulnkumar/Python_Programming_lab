num=int(input("Enter a number:"))
def factorial(num):
    n=num
    fact=1
    while(n):
        fact=fact*n
        n=n-1
    return fact
fact_num=factorial(num)
print("Factorial of ",num,"is",fact_num) 
