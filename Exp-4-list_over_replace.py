values=input("Enter a list of values:")
int_values=list(map(int,values.split()))
for i in range(0,len(int_values)):
    if int_values[i]>100:
        int_values[i]="over"
print(int_values)


        
