pairs=((2,5),(4,2),(9,8),(12,10))
count=0
for i in pairs:
    if i[0]%2==0 and i[1]%2==0:
        count+=1

print("The number of even pairs in the tuple is : ",count)