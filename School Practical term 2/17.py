import json

s=input("Enter a sentence : ")
f={}
for i in s : 
    i=i.lower()
    if i.isalnum():
        if i not in f: 
            f[i]=1
        else :
            f[i]+=1
print("Frequency of digits and letters in the sentence are : ")
print(json.dumps(f,indent=2))