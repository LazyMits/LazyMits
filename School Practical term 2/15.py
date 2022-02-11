d1= {1:40, 2:70, 3:70}
d2= {1:40, 2:50, 3:60}
d3= {1:70, 2:80, 3:90}
stu=["Suniti", "Ryna", "Zeba" ]
Student = dict(zip(stu,(d1,d2,d3)))
for i in Student :
    print("Name : ",i)
    print("Subject\t\tMarks")
    for j in Student[i]:
        print(f"{j}\t\t{Student[i][j]}")
    print()
