my_dict={}
num=int(input("Enter the number of elements in dictionary:"))
for i in range(num):
        key=input("Enter Key:")
        value=input("Enter value:")
        my_dict[key]=value
print("Dictionary sorted in ascending order by value: ",dict(sorted(my_dict.items(),key= lambda v:v[1])))
print("Dictionary sorted in descending order by value: ",dict(sorted(my_dict.items(),key= lambda v:v[1],reverse=True)))
