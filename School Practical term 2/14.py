d={"1":"1","2":"4","3":"9","4":"16","5":"25","6":"36"}
v=input("Enter the value that you want to seach for : ")
if v not in d.values() :
    print("Error : This value is not present in the dictionary")
else : 
    index = list(d.values()).index(v)
    print(f"The value {v} has the key {list(d.keys())[index]}")
