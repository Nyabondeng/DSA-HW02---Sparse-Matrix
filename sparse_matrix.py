class SparseMatrix:
    """
    Represents a sparse matrix.

    Attributes:
        numRows (int): The number of rows in the matrix.
        numCols (int): The number of columns in the matrix.
        elements (dict): A dictionary containing the non-zero elements of the matrix.
            The keys are tuples representing the (row, column) indices, and the values are the corresponding elements.
    """

    def __init__(self, matrixFilePath=None, numRows=None, numCols=None):
        """
        Initializes a SparseMatrix object.

        Args:
            matrixFilePath (str, optional): The path to a file containing the matrix data.
            numRows (int, optional): The number of rows in the matrix.
            numCols (int, optional): The number of columns in the matrix.

        Raises:
            ValueError: If neither matrixFilePath nor numRows and numCols are provided.
        """
        if matrixFilePath:
            self.read_from_file(matrixFilePath)
        elif numRows is not None and numCols is not None:
            self.numRows = numRows
            self.numCols = numCols
            self.elements = {}
        else:
            raise ValueError("Either matrixFilePath or numRows and numCols must be provided")

    def read_from_file(self, matrixFilePath):
        """
        Reads the matrix data from a file.

        The file should have the following format:
        - The first line should be "rows=<numRows>", where <numRows> is the number of rows in the matrix.
        - The second line should be "cols=<numCols>", where <numCols> is the number of columns in the matrix.
        - The remaining lines should contain the non-zero elements of the matrix in the format "(row, col, value)".

        Args:
            matrixFilePath (str): The path to the file.

        Raises:
            ValueError: If the file has an incorrect format.
            ValueError: If there is an error reading the file.
        """
        self.elements = {}
        try:
            with open(matrixFilePath, 'r') as file:
                lines = file.readlines()
                print(f"Read {len(lines)} lines from {matrixFilePath}")
                self.numRows = int(lines[0].split('=')[1].strip())
                self.numCols = int(lines[1].split('=')[1].strip())
                for i, line in enumerate(lines[2:], start=3):  # Start counting lines from 3 for better error messages
                    if line.strip():
                        line = line.strip()
                        print(f"Processing line {i}: {line}")
                        if line[0] != '(' or line[-1] != ')':
                            raise ValueError(f"Input file has wrong format at line {i}: {line}")
                        row, col, value = map(int, line[1:-1].split(','))
                        self.elements[(row, col)] = value
        except ValueError as e:
            print(f"Error processing line: {line}")
            raise ValueError("Input file has wrong format") from e
        except Exception as e:
            raise ValueError("Error reading file") from e

    def getElement(self, currRow, currCol):
        """
        Gets the element at the specified row and column indices.

        Args:
            currRow (int): The row index.
            currCol (int): The column index.

        Returns:
            int: The element at the specified indices. Returns 0 if the element is not present in the matrix.
        """
        return self.elements.get((currRow, currCol), 0)

    def setElement(self, currRow, currCol, value):
        """
        Sets the element at the specified row and column indices.

        If the value is 0, the element is removed from the matrix.

        Args:
            currRow (int): The row index.
            currCol (int): The column index.
            value (int): The value to set.
        """
        if value != 0:
            self.elements[(currRow, currCol)] = value
        elif (currRow, currCol) in self.elements:
            del self.elements[(currRow, currCol)]

    def __add__(self, other):
        """
        Adds two sparse matrices.

        Args:
            other (SparseMatrix): The matrix to add.

        Returns:
            SparseMatrix: The result of the addition.

        Raises:
            ValueError: If the dimensions of the matrices do not match.
        """
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrices dimensions do not match for addition")
        result = SparseMatrix(numRows=self.numRows, numCols=self.numCols)
        for key in set(self.elements.keys()).union(other.elements.keys()):
            result.setElement(key[0], key[1], self.getElement(key[0], key[1]) + other.getElement(key[0], key[1]))
        return result

    def __sub__(self, other):
        """
        Subtracts two sparse matrices.

        Args:
            other (SparseMatrix): The matrix to subtract.

        Returns:
            SparseMatrix: The result of the subtraction.

        Raises:
            ValueError: If the dimensions of the matrices do not match.
        """
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrices dimensions do not match for subtraction")
        result = SparseMatrix(numRows=self.numRows, numCols=self.numCols)
        for key in set(self.elements.keys()).union(other.elements.keys()):
            result.setElement(key[0], key[1], self.getElement(key[0], key[1]) - other.getElement(key[0], key[1]))
        return result

    def __mul__(self, other):
        """
        Multiplies two sparse matrices.

        Args:
            other (SparseMatrix): The matrix to multiply.

        Returns:
            SparseMatrix: The result of the multiplication.

        Raises:
            ValueError: If the dimensions of the matrices do not match.
        """
        if self.numCols != other.numRows:
            raise ValueError("Matrices dimensions do not match for multiplication")
        result = SparseMatrix(numRows=self.numRows, numCols=other.numCols)
        for (i, k) in self.elements:
            for j in range(other.numCols):
                result.setElement(i, j, result.getElement(i, j) + self.getElement(i, k) * other.getElement(k, j))
        return result

    def __str__(self):
        """
        Returns a string representation of the sparse matrix.

        Returns:
            str: The string representation of the matrix.
        """
        elements_str = [f"({r}, {c}, {v})" for (r, c), v in self.elements.items()]
        return f"rows={self.numRows}\ncols={self.numCols}\n" + "\n".join(elements_str)
