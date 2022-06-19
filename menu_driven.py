from types import NoneType
from matrix import *

print("\nWelcome to Matrix Calaculator\n\nCreate Matrix:")
m1 = matrix(int(input("\nEnter Number of Colomn: ")),int(input("Enter Number of Row: ")))
while True:
    print('''\n
    Choose one of the following:

    1. Matrix Addition
    2. Matrix Subtraction
    3. Matrix Multiplication
    4. Minor/Minors of a Matrix 
    5. Cofactor Matrix
    6. Transpose of a Matrix
    7. Adjoint of a Matrix
    8. Determinant of a Matrix
    9. Inverse of a Matrix
    0. Quit        
    ''')
    choice = int(input("\nEnter choice: "))

    if choice == 1:
        matrix_addition(m1)
    
    elif choice == 2:
        matrix_subtraction(m1)

    elif choice == 3:
        matrix_multiplication(m1)
    
    elif choice == 4:
        minors_of_matrix(m1)
    
    elif choice == 5:
        cofactor=cofactor_matrix(m1)
        if cofactor is not NoneType:
            print('\nCofactor Matrix of')
            display_matrix(m1)
            print('is: ')
            display_matrix(cofactor)
        else:
            print("\nCofactor Matrix can't be found, no of rows and no of columns must be equal")
    
    elif choice == 6:
        print('\nTranspose of')
        display_matrix(m1)
        print('is: ')
        display_matrix(transpose_of_matrix(m1))

    elif choice == 7:
        adjoint=adjoint_of_matrix(m1)
        if adjoint is not NoneType:
            print('\nAdjoint Matrix of the matrix')
            display_matrix(m1)
            print('is: ')
            display_matrix(adjoint)
        else:
            print("\nAdjoint Matrix can't be found, no of rows and no of columns must be equal")

    elif choice == 8:
        determinant=determinant_of_matrix(m1)
        if determinant is not NoneType:
            print('\nDeterminat of the Matrix')
            display_matrix(m1)
            print(f'is: {determinant}')
        else:
            print("\nDeterminant of the Matrix can't be found, no of rows and no of columns must be equal")
    
    elif choice == 9:
        inverse=inverse_of_matrix(m1)
        if inverse is not NoneType:
            print('\nInverse of the Matrix')
            display_matrix(m1)
            print('is: ')
            display_matrix(inverse)
        else:
            print("\nDeterminant of the Matrix can't be found, no of rows and no of columns must be equal")

    else:
        break