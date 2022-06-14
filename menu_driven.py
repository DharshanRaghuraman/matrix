from matrix import *

m1 = matrix(int(input("Enter Number of Colomn: ")),int(input("Enter Number of Row: ")))
m2 = matrix(int(input("Enter Number of Colomn: ")),int(input("Enter Number of Row: ")))
print('matrix 1 is :')
display_matrix(m1)
print('matrix 2 is :')
display_matrix(m2)

while True:
    choice = int(input("Enter choice: "))
    if choice == 1:
        m3 = matrix_addition(m1, m2)
        display_matrix(m3)
    elif choice == 2:
        m3 = matrix_subtraction(m1, m2)
        display_matrix(m3)
    elif choice == 3:
        m3 = matrix_multiplication(m1, m2)
        display_matrix(m3)
    elif choice == 4:
        print('determinant of')
        display_matrix(m1)
        print('is ', determinant(m1))

        print()

        print('determinant of')
        display_matrix(m2)
        print('is ', determinant(m2))
    elif choice == 0:
        break