def spiralOrder(A):
    m = len(A)
    n = len(A[0])
    T,B = 0,m-1
    L,R = 0,n-1
    dir = 0
    spiral = []
    while T<=B and L<=R:
        if dir == 0:
            for i in range(L,R+1): spiral.append(A[T][i])
            T += 1
        elif dir == 1:
            for i in range(T,B+1): spiral.append(A[i][R])
            R -= 1
        elif dir == 2:
            for i in range(R,L-1,-1): spiral.append(A[B][i])
            B -= 1
        else:
            for i in range(B,T-1,-1): spiral.append(A[i][L])
            L += 1
        dir = (dir+1)%4
    return spiral
A = [(1,2,3),(4,5,6),(7,8,9)]
print(spiralOrder(A))