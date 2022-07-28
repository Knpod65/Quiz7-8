def CM(m): #CM(m) is assigned for the reason that show how to begin and stop matrix.
    def CD(i,j,m): #CD's function is defined because arranged matrix.
        def IF(i,j,m): #function OF 'IF' is determined by the condition.
            h=""
            if i<j and j != m:
                h+=" 0"
            elif i==j or j==m:
                h+=" 1"
            else:
                h+="-1"
            return h
        
        g=""
        if j != m:
            g+=IF(i,j,m)
            g+=". "
        else:
            g+=IF(i,j,m)
            g+="."
        return g
    
    def FR(i,m): #FR's function is imposed about what function can run on column and row together.
        z=""
        if i != m:
            for j in range(1,m+1):
                z+=CD(i,j,m)
            z+="]\n"
        else:
            for j in range(1,m+1):
                z+=CD(i,j,m)
            z+="]"
        return z
    
    c="["
    for i in range(1,m+1):
        if i ==1:
            c+="["
            c+=FR(i,m)
        else:
            c+=" ["
            c+=FR(i,m)
    c+= "]"
    return c

m=int(input("Put your order to make the square matrix (m): "))
print(CM(m)) #this show result in this quiz.