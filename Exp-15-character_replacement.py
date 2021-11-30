string=input("Enter a string:")
new_str=[]
for i in string:
    new_str.append(i)
first_char=new_str[0]
for i in range(1,len(new_str)):
    if new_str[i]==first_char:
        new_str[i]="$"
replaced_str=''.join(map(str,new_str))
print("New string:"+replaced_str)
