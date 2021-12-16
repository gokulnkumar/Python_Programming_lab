limit=int(input("Enter the limit:"))
def fibonacci(limit):
    i=0
    j=1
    k=0
    if limit==1:
        print(i)
        return
    for x in range(1,limit+1):
        print(k)
        i=j
        j=k
        k=i+j
print("Fibonacci series upto ",limit," is:")
fibonacci(limit)

        
        
