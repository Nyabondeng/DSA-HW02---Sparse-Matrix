**SparseMatrix**

Overview

This project implements a sparse matrix data structure in Python. The SparseMatrix class optimizes both memory and runtime while storing large matrices with mostly zero elements. The implementation includes functionality to read sparse matrices from a file, perform addition, subtraction, and multiplication operations on them, and handle different input variations.

**Features**

Initialization: Initialize the SparseMatrix from a file or create an empty matrix with specified dimensions.
File Reading: Read and parse a sparse matrix from a file.
Element Access: Get and set elements of the sparse matrix.
Addition: Add two sparse matrices.
Subtraction: Subtract one sparse matrix from another.
Multiplication: Multiply two sparse matrices.
String Representation: Get a string representation of the sparse matrix.

**Code Documentation**

**SparseMatrix Class**
__init__(self, matrixFilePath=None, numRows=None, numCols=None): Initializes the SparseMatrix object. Loads matrix from a file or creates an empty matrix with given dimensions.

read_from_file(self, matrixFilePath): Reads the sparse matrix from a file and stores it in the elements dictionary. Raises an error if the file format is incorrect.

getElement(self, currRow, currCol): Returns the value of the element at the specified row and column. Returns 0 if the element is not explicitly stored.

setElement(self, currRow, currCol, value): Sets the value of the element at the specified row and column. If the value is 0, the element is removed from the dictionary.

__add__(self, other): Adds two sparse matrices. Returns a new SparseMatrix representing the sum. Raises an error if the dimensions do not match.

__sub__(self, other): Subtracts one sparse matrix from another. Returns a new SparseMatrix representing the difference. Raises an error if the dimensions do not match.

__mul__(self, other): Multiplies two sparse matrices. Returns a new SparseMatrix representing the product. Raises an error if the number of columns of the first matrix does not match the number of rows of the second matrix.

__str__(self): Returns a string representation of the sparse matrix.


