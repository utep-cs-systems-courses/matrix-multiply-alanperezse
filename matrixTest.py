from matrixUtils import multiplyMatrix, multiplyMatrixBlock, multiplyMatrixParallel, genMatrix, printSubarray
import argparse
import time


def testMultBlock():
    mat = genMatrix(400, 1)

    mat = multiplyMatrixBlock(mat, mat)
    for i in range(400):
        for j in range(400):
            assert mat[i][j] == 400
    print('Matrix block multiplication successful')


def testParallelMatrix():
    mat = genMatrix(400, 1)
    mat = multiplyMatrixParallel(mat, mat)
    for i in range(400):
        for j in range(400):
            assert mat[i][j] == 400
    print('Parallel multiplication successful')


def testMultMatrix():
    mat1 = [[1, 2, 3],
            [4, 5, 6]]
    mat2 = [[10, 11],
            [20, 21],
            [30, 31]]
    mat_expected = [[140, 146],
                    [320, 335]]

    mat = multiplyMatrix(mat1, mat2)

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            assert mat_expected[i][j] == mat[i][j]

    mat = genMatrix(400, 1)

    mat = multiplyMatrixBlock(mat, mat)
    for i in range(400):
        for j in range(400):
            assert mat[i][j] == 400

    print('Regular multiplication successful')


parser = argparse.ArgumentParser(description=
        'Tests for the different methods of the matrixUtils module.'
        'If indicated, it may iteratively perform multiple matrix'
        'multiplications to evaluate the performance of the algorithm')
parser.add_argument('-i', '--iterations', default=-1, type=int,
        help='Number of matrix multiplications to perform.')
parser.add_argument('-a', '--alternative', action='store_true',
        help = 'Use the alternative multiply algorithm during -i testing.'
        '(requires square matrices).')
parser.add_argument('-p', '--parallel', action='store_true',
        help = 'Use the parallel algorithm during -i testing.')
parser.add_argument('-s', '--size', default=1024, type=int,
        help='Size of the 2d matrices to be multiplied during -i testing.')

args = parser.parse_args()

if args.iterations >= 0:
    n = args.iterations
    mat1 = genMatrix(args.size, 1)
    mat2 = genMatrix(args.size, 1)

    total_time = 0

    for i in range(0, n):
        print(f'Performing multiplication number {i + 1}:', end = ' ')
        t0 = time.clock_gettime(time.CLOCK_MONOTONIC_RAW)
        if args.parallel:
            mat = multiplyMatrixParallel(mat1, mat2)
        elif args.alternative:
            mat = multiplyMatrixBlock(mat1, mat2)
        else:
            mat = multiplyMatrix(mat1, mat2)
        t1 = time.clock_gettime(time.CLOCK_MONOTONIC_RAW)
        print(t1 - t0)
        total_time += t1 - t0

    print(f'Completed iterations. Avg time: {total_time / n}')
else:
    testMultMatrix()
    testMultBlock()
    testParallelMatrix()
    print('All tests successful')
