#!/usr/bin/env python3
import argparse
import numpy as np
import time
import pymp


def genMatrix(size=1024, value=1):
    """
    Generates a 2d square matrix of the specified size with the specified values
    """
    matrix = [[value for col in range(size)] for row in range(size)]

    return matrix

def genMatrix2(size=1024, value=1):
    """
    Generates a 2d square matrix of the specified size with the specified values
    """
    matrix = np.asarray([np.asarray([value for col in range(size)]) for row in range(size)])

    return matrix

def multiplyMatrix(matrix1, matrix2):
    # Test for compatibility
    # Test len of rows for matrix1 and len of cols for matrix2
    if not len(matrix1[0]) == len(matrix2):
        return None

    num_rows_1 = len(matrix1)       # Num of rows in matrix 1
    num_cols_2 = len(matrix2[0])    # Num of cols in matrix 2
    num_common = len(matrix1[0])    # Num of cols in matrix 1 / rows in matrix 2

    # Create return matrix
    rtn = [[0 for _ in range(num_cols_2)] for _ in range(num_rows_1)]

    # Assign correct values
    for i in range(num_rows_1):
        for j in range(num_cols_2):
            # Calculate sum
            for k in range(num_common):
                rtn[i][j] += matrix1[i][k] * matrix2[k][j]

    return rtn


def multiplyMatrixParallel(matrix1, matrix2):
    # Test for compatibility
    # Test len of rows for matrix1 and len of cols for matrix2
    if not len(matrix1[0]) == len(matrix2):
        return None

    num_rows_1 = len(matrix1)       # Num of rows in matrix 1
    num_cols_2 = len(matrix2[0])    # Num of cols in matrix 2
    num_common = len(matrix1[0])    # Num of cols in matrix 1 / rows in matrix 2

    # Create return matrix
    #rtn = [[0 for _ in range(num_cols_2)] for _ in range(num_rows_1)]
    rtn = [pymp.shared.list([0 for _ in range(num_cols_2)]) for _ in range(num_rows_1)]

    # Assign correct values
    with pymp.Parallel() as p:
        for i in p.range(num_rows_1):
            for j in range(num_cols_2):
                # Calculate sum
                for k in range(num_common):
                    rtn[i][j] += matrix1[i][k] * matrix2[k][j]
    return rtn


def multiplyMatrixBlock(matrix1, matrix2):
    # Test for compatibility
    if not len(matrix1) == len(matrix1[0]) == len(matrix2) == len(matrix2[0]):
        return None

    size = len(matrix1)       # Size of all sides
    # Create return matrix
    rtn = [[0 for _ in range(size)] for _ in range(size)]


    step = 16

    for kk in range(0, size, step):
        for jj in range(0, size, step):
            for i in range(size):
               j_end_val = jj + step
               for j in range(jj, min(j_end_val, size)):
                  k_end_val = kk + step
                  sum = rtn[i][j]
                  for k in range(kk, min(k_end_val, size)):
                    sum = sum + matrix1[i][k] * matrix2[k][j]
                  rtn[i][j] = sum

    return rtn


def printSubarray(matrix, size=10):
    """
    Prints the upper left subarray of dimensions size x size of
    the matrix
    """
    for row in range(min(10, len(matrix))):
        for col in range(min(10, len(matrix[row]))):
            print(f'{matrix[row][col]} ' , end='')
        print('')

def writeToFile(matrix, fileName):
    """
    Writes a matrix out to a file
    """
    with open(fileName, 'w') as file:
        for row in matrix:
            for col in row:
                file.write(f'{col} ')
            file.write('\n')

def readFromFile(fileName):
    """
    Reads a matrix from a file
    """
    matrix = []

    with open(fileName, 'r') as file:
        for line in file:
            row = [int(val) for val in line.split()]
            matrix.append(row)

    return matrix


def main():
    """
    Used for running as a script
    """
    parser = argparse.ArgumentParser(description=
        'Create a matrix of specified size and values, or create'
        'a matrix which is the product of the given matrices,')

    parser.add_argument('-s', '--size', default=1024, type=int,
        help='Size of the 2d matrix to generate.')
    parser.add_argument('-v', '--value', default=1, type=int,
        help='The value with which to fill the array with.')
    parser.add_argument('-m', '--multiply', nargs = 2,
        help = 'Filenames for the matrices to be used.')
    parser.add_argument('-a', '--alternative', action='store_true',
        help = 'Use the alternative multiply algorithm (requires square matrices).')
    parser.add_argument('-f', '--filename', type = str,
        help='The name of the file to save the matrix in (optional).')
    parser.add_argument('-p', '--parallel', action='store_true',
        help = 'Use the parallel algorithms')

    args = parser.parse_args()

    # Create matrix by multiplying
    if args.multiply:
        mat1 = readFromFile(args.multiply[0])
        mat2 = readFromFile(args.multiply[1])

        t0 = time.clock_gettime(time.CLOCK_MONOTONIC_RAW)
        if args.parallel:
            mat = multiplyMatrixParallel(mat1, mat2)
        elif args.alternative:
            mat = multiplyMatrixBlock(mat1, mat2)
        else:
            mat = multiplyMatrix(mat1, mat2)
        t1 = time.clock_gettime(time.CLOCK_MONOTONIC_RAW)
        print(f"Time taken to do matrix multiplication: {t1 - t0}")

        if mat is None:
            raise ValueError("Matrices must be compatible, and be squared if the -a flag was raised. Press -h for help")

        # Write if indicated. Always prints
        if args.filename is not None:
            print(f'Writing matrix to {args.filename}')
            writeToFile(mat, args.filename)

            print(f'Testing file')
            printSubarray(readFromFile(args.filename))
        else:
            printSubarray(mat)

    # Create matrix by using the getMatrix method
    else:
        mat = genMatrix(args.size, args.value)

        # Write if indicated. Always prints
        if args.filename is not None:
            print(f'Writing matrix to {args.filename}')
            writeToFile(mat, args.filename)

            print(f'Testing file')
            printSubarray(readFromFile(args.filename))
        else:
            printSubarray(mat)


if __name__ == '__main__':
    # execute only if run as a script
    try:
        main()
    except ValueError as e:
        print(e)
        print("Exiting the program...")
