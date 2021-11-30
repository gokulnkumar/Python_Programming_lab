string=input("Enter a string:").split(" ")
word_count=0
words={}
word_occ={}
for i in range(0,len(string)):
    if string[i] not in words.keys():
        words[string[i]]=1
    else:
        s=words[string[i]]
        s=s+1
        words[string[i]]=s
for i in words:
    print(i,":",words[i])
               

    
        
        
