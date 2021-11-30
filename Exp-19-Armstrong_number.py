num=int(input("Enter a number:"))
n=num
order=len(str(num))
sum=0
while n:
    rem=n%10
    sum=sum+(rem**order)
    n=n//10
if sum==num:
    print(num,"is a armstrong number")
else:
    print(num,"is not a armstrong number")
