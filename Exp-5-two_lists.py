list1=list(map(int,input("Enter first list of values:").split()))
list2=list(map(int,input("Enter second list of values:").split()))
if len(list1)==len(list2):
    print("Both list are of same length")
list1_sum=sum(list1)
list2_sum=sum(list2)
if list1_sum==list2_sum:
    print("Both  list sum to same nuber")
same_value=[]
for i in list1:
    if i in list2:
        same_value.append(i)
print("The following values occur in both list:",same_value)
