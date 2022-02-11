n=[]
l=int(input("Enter the number of elements in the list : "))
for i in range(l) :
    n.append(input(f"Enter the element {i+1} of the list : "))
print("List before rotating the elements :",n)
print("The list after rotating the elements :",end=" ")
n.insert(0,n.pop())
print(n)