

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


def display_matrix(m):
    for i in range(len(m)):
        print("[", end=" ")
        for j in range(len(m[i])):
            print(m[i][j], end=" ")
        print("]")

# a=matrix()
# b=matrix_addition()
# c=matrix_subtraction()
# d=matrix_multiplication()



m1 = matrix(int(input("Enter Number of Colomn: ")),int(input("Enter Number of Row: ")))
m2 = matrix(int(input("Enter Number of Colomn: ")),int(input("Enter Number of Row: ")))
print('matrix 1 is :')
display_matrix(m1)
print('matrix 1 is :')
display_matrix(m2)

while True:
    choice = int(input("Enter choice: "))
    if choice == 1:
        m3 = matrix_addition(m1,m2)
        display_matrix(m3)
    elif choice == 2:
        m3 = matrix_subtraction(m1,m2)
        display_matrix(m3)
    elif choice == 3:
        m3 = matrix_multiplication(m1,m2)
        display_matrix(m3)
    elif choice == 0:
        break

