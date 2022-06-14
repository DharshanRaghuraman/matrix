def matrix(m, n):
    L1 = []
    for i in range(m):
        L2 = []
        for j in range(n):
            ele = int(input(f"Enter Element of (Colomn,row) -> ({i+1},{j+1}): "))
            L2.append(ele)
        L1.append(L2)
    return L1


def matrix_addition(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        l1 = []
        for i in range(len(m1)):
            l2 = []
            for j in range(len(m2[0])):
                a = m1[i][j]+m2[i][j]
                l2.append(a)
            l1.append(l2)
        return l1
    else:
        print("The matrices provided are not of the same order, can't be added ")


def matrix_subtraction(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        l1 = []
        for i in range(len(m1)):
            l2 = []
            for j in range(len(m2[0])):
                a = m1[i][j]-m2[i][j]
                l2.append(a)
            l1.append(l2)
        return l1
    else:
        print("The matrices provided are not of the same order, can't be subtracted ")


def matrix_multiplication(m1, m2):
    if len(m1[0]) == len(m2):
        l1 = []
        for i in range(len(m1)):
            l2 = []
            for j in range(len(m2[0])):
                a = 0
                for k in range(len(m2)):
                    a += m1[i][k]*m2[k][j]
                l2.append(a)
            l1.append(l2)
        return l1


def determinant(m):
    if len(m) == 1:
        d = m[0][0]
        return d
    elif len(m) == 2:
        d = m[0][0] * m[1][1] - m[0][1] * m[1][0]
        return d
    elif len(m) == 3:
        a = m[0][0]
        b = m[0][1]
        c = m[0][2]

        m1 = [[m[1][1], m[1][2]],
              [m[2][1], m[2][2]]]
        
        m2 = [[m[1][0], m[1][2]],
              [m[2][0], m[2][2]]]
        
        m3 = [[m[1][0], m[1][1]],
              [m[2][0], m[2][1]]]
        
        d = a*determinant(m1) - b*determinant(m2) + c*determinant(m3)
        return d


def transpose(m):
    l1=[]
    for i in range(len(m)):
        l2=[]
        for j in range(len(m[0])):
            l2.append(m[j][i])
        l1.append(l2)
    return l1


def display_matrix(m):
    for i in range(len(m)):
        print("[", end=" ")
        for j in range(len(m[i])):
            print(m[i][j], end=" ")
        print("]")

