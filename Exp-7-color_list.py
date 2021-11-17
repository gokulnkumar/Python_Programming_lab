color_list1=input("Enter colors in list1:").split(" ")
color_list2=input("Enter colors in list2:").split(" ")
color_list=[i for i in color_list1 if i not in color_list2]
print(color_list)
