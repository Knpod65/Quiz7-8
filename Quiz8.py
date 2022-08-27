import numpy as np #import indispensable function that will recall in this quiz name numpy
def q(m, matrix): #define the function that I will use in this quiz.
    for i in range(m): #this is for-loop about i that means column on this matrix and it repeats until it is m (column) 
        a =[]  #when it starts on next row, it will begin and reset list of a is empty
        for j in range(m): #this is for-loop about j that means column on this matrix and it repeats until it is m (row)
            if i<j and j!=m: #condition of this qiuz
                a.append(0) #append 0 when this condition is TRUE in list of a
            elif i==j or j==m: #condition of this qiuz
                a.append(1) #append 1 when this condition is TRUE in list of a
            else: #condition of this qiuz
                a.append(-1) #append -1 when all previous conditions is FALSE in list of a
        matrix.append(a) #append column in matrix
matrix=[] #begin empty list to recieve every list that will produce list of list
m=int(input("Put your order to make the square matrix (m): ")) #input value what I use to make the square matrix
q(m,matrix) #this recall the function that relate between empty matrix and count of row or column: n(row) equals n(column)
matrix=np.array(matrix).reshape(R,R) # when array function works, list will be aggregated about what's column and row by matrix's list
# we will reshape it on general the square matrix
print(matrix)