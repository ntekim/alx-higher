#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def square(num):
        return num **2
    new_matrix = []
    new_inner_matrix = []
    inner_matrix = []
    length = len(matrix)
    for i in range(length):
        inner_matrix.append(matrix[i])
        for x in range(len(inner_matrix)):
            new_inner_matrix.append(matrix[i][x]**2)
            print(inner_matrix)
        new_matrix.append(new_inner_matrix)
    #print(new_matrix)
    """for n in range(len(i)):
            print("{}".format(n))
            squared = square(inner_matrix[n])
            inner_matrix[i] = int(squared)
        new_inner_matrix.append(inner_matrix)
        print(new_inner_matrix)
        new_matrix.append(new_inner_matrix)"""
    #[[row[i] for row in matrix] for i in range(len(inner 

    return new_matrix
    

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(square_matrix_simple(matrix))
