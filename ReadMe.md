# Parallel Computing Matrix Multiply Assignment

This repository contains some basic Python utilities for
matrix operations. This is also the repository where
you will submit the assignment.

Once completed the repository should contain your code,
a short report, and any instructions needed to run your
code.

# Report:

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
- If you would like to create a matrix by using the
genMatrix method, simply omit the -m flag. The values and
size of the matrix may be specified using the -v and -s
flags, respectively (optional).
- In either case, if you would like to save the matrix just
created, use the -f or --filename flags and specify the
name of the file where the matrix is to be saved
(optional).

matrixTest may be used as follows:
- You may execute the file without passing any options. This
will simply run the test methods that have been hard coded,
and show their success or failure.
- If you would like to evaluate the time for multiple matrix
multiplications, raise the -i flag and pass the number of
repeated iterations to do. You can indicate the method to use
the block or parallel algorithms by raising the -a or -p flag
respectively (you shouldn't raise both flags). The size of
the repeated matrices to be multiplied may be specified by
the -s flag.

### Issues:
Previously, the block algorithm wouldn't work for arrays of certain size. By using a min() on one of the loops, the issue was fixed. Currently, the method cannot accept arrays that are not squared.

As of now, the parallel part of the program is not running as expected. It is taking longer than the linearized version.

### Time:
The linearized version of the matrix multiplication, and the block algorithm were implemented in less than a day. The logic and the structure of how the program handles flags took more due to the desire to make one file do too much.

The parallel algorithm is still in progress. I have been working on it for a little over 3 hours now.

### Observations:
The algorithm for matrix multiplication was initially unnecessarily complicated. I have since made it more concise and readable.
