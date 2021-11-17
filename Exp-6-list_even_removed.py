list1=input("Enter a list of numbers:")
list1=list(map(int,list1.split(" ")))
list_odd=[i for i in list1 if i%2!=0]
print(list_odd)
