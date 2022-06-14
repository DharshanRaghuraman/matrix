from matrix import *

print("Matrix 1: ")
m1 = matrix(int(input("Enter Number of Colomn: ")),int(input("Enter Number of Row: ")))
print("\nMatrix 2: ")
m2 = matrix(int(input("Enter Number of Colomn: ")),int(input("Enter Number of Row: ")))
print('\nMatrix 1 is :')
display_matrix(m1)
print('\nMatrix 2 is :')
display_matrix(m2)

while True:
    choice = int(input("\nEnter choice: "))
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
        print('\nDeterminant of')
        display_matrix(m1)
        print(f'is: {determinant(m1)}')
       

        print('\nDeterminant of')
        display_matrix(m2)
        print(f'is: {determinant(m2)}')
        

    elif choice == 5:
        print('\nTranspose of')
        display_matrix(m1)
        print('is: ')
        display_matrix(transpose(m1))

        print('Transpose of')
        display_matrix(m2)
        print('is: ')
        display_matrix(transpose(m2))

    elif choice == 0:
        break