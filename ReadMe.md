# Parallel Computing Matrix Multiply Assignment

This repository contains some basic Python utilities for
matrix operations. This is also the repository where
you will submit the assignment.

Once completed the repository should contain your code,
a short report, and any instructions needed to run your
code.

# Report:
    Student: Alan Perez
    CS 4175 12PM

### Intructions:
There are two important files in the directory,
matrixUtils.py, and matrixTest.py.

matrixUtils may be used as follows:
- You may create a matrix by using the genMatrix method, or
by performing a matrix multiplication.
- If you would like to create a matrix by performing a
matrix multiplication, raise the flag -m or
--multiplication and pass the name of the files where the
two matrices to be multiplied are located. You may use
the tile algorithm by raising the -a or --alternative
flag (optional).

  For instance: python3 matrixUtils -m matrix1 matrix2 -a

- If you would like to create a matrix by using the
genMatrix method, simply omit the -m flag. The values and
size of the matrix may be specified using the -v and -s
flags, respectively (optional).

  For instance: python3 matrixUtils -s 10 -v 4

- In either case, if you would like to save the matrix just
created, use the -f or --filename flags and specify the
name of the file where the matrix is to be saved
(optional).

  For instance: python3 matrixUtils -s 10 -v 4 -f matrix1

matrixTest may be used as follows:
- You may execute the file without passing any options. This
will simply run the test methods that have been hard coded,
and show their success or failure.

  For instance: python3 matrixTest

- If you would like to evaluate the time for multiple matrix
multiplications, raise the -i flag and pass the number of
repeated iterations to do. You can indicate the method to use
the block or parallel algorithms by raising the -a or -p flag
respectively (you shouldn't raise both flags). The size of
the repeated matrices to be multiplied may be specified by
the -s flag.

  For instance: python3 matrixTest -i 10 -s 10

### Issues:
Previously, the block algorithm wouldn't work for arrays of certain size. By using a min() on one of the loops, the issue was fixed. Currently, the method cannot accept arrays that are not squared.

The major issue with the parallel algorithm was how to properly make use of the pymp.Parallel for nested lists. The
problem was fixed by making use of the pymp.shared.array() method that can create a 2D numpy array.

As of now, the parallel part of the program is giving back the right results, although it is taking longer than the linearized version. This might be a Virtual Machine issue.


### Time:
The linearized version of the matrix multiplication, and the block algorithm were implemented in less than a day. The logic and the structure of how the program handles flags took more due to the desire to make one file do too much.

The parallel algorithm has taken around 4 hours to do due to errors with the results. It has finally been completed.

### Performance measurements:
The following measurements are an average of repeatedly multiplying a square matrix
with size of 350 by itself, 10 times.

1 thread:   11.0525 seconds

2 threads:  10.4618 seconds

4 threads:  5.7258 seconds

8 threads:  5.9441 seconds


### Analysis:
The run with 4 threads seems to be the quickest. Although we have more than 8 processes (matrix multiplications
algorithm does parallelization over the rows of matrix1), it seems that the additional overhead of those processes
does more damage than the benefit from the extra threads. This might change if we were to use bigger arrays, since
I did notice when testing even smaller arrays that the most efficient number of threads was 1 or 2.


### Observations:
The algorithm for matrix multiplication was initially unnecessarily complicated. I have since made it more concise and readable.

The block algorithm currently only works for square matrices.

The parallel algorihtm outputs the correct results, although is slower than the linear algorithm. The number of
threads that make the algorithm more efficient depends on the size of the array (due to the overhead of the
parallel process). Bigger arrays tend to perform better with more cores.


### Output from cpuInfoDump program:
model name      : Intel(R) Core(TM) i5-7200U CPU @ 2.50GHz

      4      36     216
