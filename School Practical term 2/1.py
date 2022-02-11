# using list comprehension 


matrix = [[1,2,3],[4,5,6],[7,8,9]]
t_matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
print("The transpose of the matrix is ")
for i in t_matrix : 
    print(i)


# using only lists 

matrix = [[1,2,3],[4,5,6],[7,8,9]]
t_matrix = []

for i in range(len(matrix[0])) :
    t_matrix.append([])

for i in range(len(matrix[0])) :
    for j in range(len(matrix)) :
        t_matrix[i].append(matrix[j][i])

print("The transpose of the matrix is ")
for i in t_matrix :
    print(i)
