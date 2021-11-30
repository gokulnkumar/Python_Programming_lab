num=int(input("Enter a number:"))
rem=0
rev=0
while num:
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
print("Reverse of the number is:",rev)
