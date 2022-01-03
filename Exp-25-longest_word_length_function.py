words=input("Enter a list of words:").split(" ")
def longest_word(words):
    length=0
    for i in words:
        if len(i)>length:
            length=len(i)
            return length
max_length=longest_word(words)
print("Longest length:",max_length)
    
