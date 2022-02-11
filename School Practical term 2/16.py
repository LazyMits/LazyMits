keys=[i for i in range(10)]
Dct = dict.fromkeys(keys,200)
print("Dictionary before updation : ",Dct)
Dct[0]+=200
Dct[9]+=200
print("New Updated Dictionary is  : ",Dct)
