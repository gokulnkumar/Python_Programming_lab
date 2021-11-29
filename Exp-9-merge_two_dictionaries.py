dict1={}
dict2={}
dict3={}
n1=int(input(("Enter number of elements in dictionary 1:")))
for i in range(n1):
    key=input("Enter Key:")
    value=input("Enter Value:")
    dict1[key]=value
n2=int(input(("Enter number of elements in dictionary 2:")))
for i in range(n2):
    key=input("Enter Key:")
    value=input("Enter Value:")
    dict2[key]=value
dict3=dict1.copy()
dict3.update(dict2)
print("Merged dictionary:",dict3)
