str1=input("Enter a string:")
vowels=['a','e','i','o','u']
vowels_list=[i for i in str1.lower() if i in vowels]
print(vowels_list)
