d1= {1:100, 2:200, 3:300}
d2= {1:300, 2:200, 5:400}
k=[i for i in list(d1.keys())]
for i in list(d2.keys()) :
    if i not in k:
        k.append(i)
d3={}
for i in k:
    d3[i] = d1.get(i,0)+d2.get(i,0)
print("The resultant dictionary : ",d3)