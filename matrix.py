def matrix(m=int(input("Number of Columns")), n=(int(input("Number of Rows")))):
    L1 = []
    for i in range(n):
        L2 = []
        for j in range(m):
            ele = int(input(f"Enter Element of (row,column) -> ({i+1},{j+1}): "))
            L2.append(ele)
        L1.append(L2)
    print("Matrix Created Successfully")
    display_matrix(L1)
    return L1
    

def matrix_addition(m1):
    print("Create Matrix to Add with:")
    m2=matrix()
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        l1 = []
        for i in range(len(m1)):
            l2 = []
            for j in range(len(m2[0])):
                a = m1[i][j]+m2[i][j]
                l2.append(a)
            l1.append(l2)
        print("Matrices Added Successfully")
        display_matrix(l1)
        return l1
    else:
        print("The matrices provided are not of the same order, can't be added ")


def matrix_subtraction(m1):
    print("Create Matrix to Subtract with:")
    m2=matrix()
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        l1 = []
        for i in range(len(m1)):
            l2 = []
            for j in range(len(m2[0])):
                a = m1[i][j]-m2[i][j]
                l2.append(a)
            l1.append(l2)
        print("Matrices Subtracted Successfully")
        display_matrix(l1)
        return l1
    else:
        print("The matrices provided are not of the same order, Hence can't be subtracted ")


def matrix_multiplication(m1):
    print("Create Matrix to Multiply with:")
    m2=matrix()
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
        print("Matrices Multiplied Successfully")
        display_matrix(l1)
        return l1
    else:
        print("Matrix can't be mutiplied, No of row of first matrix should be equal to no of column of second matrix")


def list_for_detreminat(m):
    if len(m)==len(m[0]):
        l1 = []
        for i in range(len(m)):
            for j in range(len(m[0])):
                l2=[]
                for k in range(len(m)):
                    if k != i:
                        l3 = []
                        for l in range(len(m[0])):
                            if l != j:
                                l3.append(m[k][l])
                        l2.append(l3)
                l1.append(l2)
        return l1


def minors_of_matrix(m):
    if len(m)==len(m[0]):
        l=list_for_detreminat(m)
        l1=[]
        for i in range(len(m)):
            for j in range(len(m[0])):
                d=determinant_of_matrix(l[i][j])
                print(l[i][j])
                l1.append(d)
        print(l1)
    else:
        print("Minor can't be found, no of rows and no of columns must be equal")


def cofactor_matrix(m):
    if len(m)==len(m[0]):
        l=list_for_detreminat(m)
        l1=[]
        for i in range(len(m)):
            l2=[]
            for j in range(len(m[0])):
                d=determinant_of_matrix(l[i][j])
                if (i+j)%2==0:
                    l2.append(d)
                else:
                    l2.append(-d)
            l1.append(l2)
        return l1


def transpose_of_matrix(m):
    l1=[]
    for i in range(len(m[0])):
        l2=[]
        for j in range(len(m)):
            l2.append(m[j][i])
        l1.append(l2)
    return l1


def adjoint_of_matrix(m):
    if len(m)==len(m[0]):
        a=cofactor_matrix(m)
        adj=transpose_of_matrix(a)
        return adj
    else:
        print("Adjoint of the matrix can't be found, no of rows and no of columns must be equal")

def determinant_of_matrix(m):
    if len(m)==len(m[0]):
        if len(m) == 1:
            d = m[0][0]

        elif len(m) == 2:
            d = m[0][0] * m[1][1] - m[0][1] * m[1][0]
            
        else:
            a=minors_of_matrix(m)
            d=0
            for i in range(len(m)):
                if i%2==0:
                    d+=m[0][i]*determinant_of_matrix(a[i])
                else:
                    d-=m[0][i]*determinant_of_matrix(a[i])
            print(f"Determinat of the Given Matrix is: {d}")
        return d
    else:
        print("Determinat can't be found, no of rows and no of columns must be equal")


def inverse_of_matrix(m):
    if len(m)==len(m[0]):
        a=cofactor_matrix(m)
        b=determinant_of_matrix(m)
        l1=[]
        for i in range(len(a[0])):
            l2=[]
            for j in range(len(a)):
                l2.append(a[j][i]/b)
            l1.append(l2)
    else:
        print("Inverse can't be found, no of rows and no of columns must be equal")


def display_matrix(m):
    for i in range(len(m)):
        print("[", end=" ")
        for j in range(len(m[i])):
            print(m[i][j], end=" ")
        print("]")

matrix()