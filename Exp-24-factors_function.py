num=int(input("Enter a number:"))
factor_list=[]
def factor(num):
    for i in range(1,num+1):
        if num%i==0:
            factor_list.append(i)
    print("Factors of ",num,"are:",factor_list)
factor(num)
            
