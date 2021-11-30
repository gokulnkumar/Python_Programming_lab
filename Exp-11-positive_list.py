num=input("Enter a list of integers:")
num=list(map(int,num.split(" ")))
positive_list=[i for i in num if i>0]
print(positive_list)
