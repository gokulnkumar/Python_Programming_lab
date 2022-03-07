num=int(input("Enter a number:"))
prime=0
if(num==1):
    prime=1
for x in range(2,num):
    if num%x==0:
        prime=1
        break
if prime==0:
    print(num,'is a prime number')
else:
    print(num,'is not a prime number')
