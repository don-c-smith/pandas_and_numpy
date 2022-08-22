import numpy as np
import pandas as pd

# Note that importing these libraries 'as' a shorter name just saves us time typing

# NumPy is a linear algebra array used for multidimensional arrays
# It combines the speed and efficiency of C with the comprehensible syntax of Python
# Here are examples of ways to work with these libraries

# First, let's define a one-dimensional array (a simple list)
list_1 = [50, 60, 80, 100, 200, 300, 500, 600]
print(list_1)

# Now, let's generate a numpy array from the list we created
my_numpy_array = np.array(list_1)
print(my_numpy_array)  # Note that this looks different now

# Printing the type of the array returns 'numpy.ndarray' which means 'multi-dimensional array'
print(type(my_numpy_array))

# You can also directly define and fill multi-dimensional numpy arrays
# You do this by creating nested lists where each sub-list is a row
# Elements in each sub-list are separated by commas
# Sub-lists (rows) are also separated by commas
my_matrix = np.array([[2, 5, 8] , [7, 3, 6]])
print(my_matrix)  # Returns an array with two rows of three columns each

# Now we can start using some basic numpy methods and functions

# Here's how to create random numbers
# Let's make a distribution of 20 random numbers between zero and 1
numbers = np.random.rand(20)
print(numbers)  # This creates 20 random numbers between zero and 1

# You can also create a matrix of random numbers
matrix = np.random.rand(3, 3)  # This creates a 3x3 matrix populated with random numbers between zero and 1
print(matrix)  # Note that the matrix has three distinct rows, each with three values

# The randint function allows you to create random integers between specified upper and lower bounds
integer = np.random.randint(1, 50)  # This creates a variable with a SINGLE random integer between 1 and 50
print(integer)  # Note that if you run the code again, you'll get a different random value within your bounds

# To generate multiple random integers, supply a third value for the numbers of integers you want generated
integers = np.random.randint(1, 100, 15)  # Generates 15 random numbers between 1 and 100
print(integers)  # Here's the list of 15 random integers
print(type(integers))  # Note that the variable is created as a numpy array

# You can also create an array of evenly-spaced values within a specified interval
even = np.arange(1, 50)
print(even)  # Note that this prints a list of all integers from 1 to 49, because 50 as the upper bound is NOT included

# You can use numpy to create 'diagonals' - basically a matrix where a specified value appears 'diagonally'
# These 'diagonals' are also called 'eyes' for some reason
diag = np.eye(7)
print(diag)  # This creates a 7x7 matrix where 1s move 'diagonally' from left to right

# You can create a matrix of a given size filled with 1s, if you want
matrix_ones = np.ones((7, 7))  # This creates a 7x7 matrix filled with 1s
print(matrix_ones)

# Here's how to create a one-dimensional array filled with zeroes
array_zeroes = np.zeros(8)  # This creates an array filled with eight zeroes
print(array_zeroes)

# Let's try a small integration/exercise
# We will create a 1x10 array of random integers ranging from 0 to 'x,' where x is a value input by the user
upper_bound_raw = input('Enter the upper-boundary integer: ')  # Start by getting the user's input
# Per best-practices, we'll use a try/except to make sure the user didn't mess up
try:
    upper_bound = int(upper_bound_raw)  # See if we can re-type the input as an integer
except:  # If not:
    print('ERROR: Not an integer')  # Send an error message
    quit()  # And quit the program
defined_values = np.random.randint(0, upper_bound, 10)  # Otherwise, pass the numpy method the input integer as a bound
print(defined_values)  # And print the array of random integers

# Let's start working with mathematical operators
# Start by defining two ranges, each filled with the integers from 1 to 9
range_1 = np.arange(1, 10)  # Note: using 10 as the top bound does not put 10 in the array - 'up to but not including'
range_2 = np.arange(1, 10)  # ibid

# We can now perform what's called 'element-by-element addition'
# This means that each element in one array will be added to its counterpart in the other array
# You can do this by just adding the array objects together
range_sum = range_1 + range_2
print(range_1)
print(range_2)
print(range_sum)
# You can see that in range_sum, the two ones have become a 2, the two 2s have become a 4, etc.

# Here's how to square each element in an array
range_square = range_1 ** 2  # Just square the array as you would normally
print(range_square)  # Each element has been squared - 1 is 1, 2 is 4, 3 is 9, etc.

# Here's how to take the square root of each element in an array
range_sqrt = np.sqrt(range_square)  # Taking the square root of each element in the squared range
print(range_sqrt)  # Note that this (as expected) puts us back at the original set of values in the unsquared range_1

# Here's how to calculate the exponent of each element in an array
range_exp = np.exp(range_1)
print(range_exp)  # Returns the exponents of each element in the array

# Now let's do some slicing and indexing of arrays - a crucial skill
# Start with a new array
array = np.array([3, 5, 6, 2, 8, 10, 20, 50])
print(array)  # We see the array with these declared values
# The first element in the array, 3, is at index position zero
# To extract the first element in the array, we call for it the same way we'd call a standard list
print(array[0])  # Returns 3

# You can also 'slice' arrays just like you would a list
print(array[:5])  # Extracting the first through the fifth elements of the array - returns [3 5 6 2 8]
# Note that this is just like what you'd do to an ordinary list

# Altering multiple values in a numpy array at once is called 'broadcasting'
# Let's change the first four elements in the array to a value of 7
array[0:4] = 7  # Set elements 1, 2, 3, and 4 equal to a value of 7
# Remember that INDEX 4 is actually ELEMENT 5 - we're doing 'up to but not including' again
print(array)  # Returns [7, 7, 7, 7, 8, 10, 20, 50]

# Here are the tools to slice and extract from multi-dimensional arrays, or matrices
# Start by creating a 4x4 matrix filled with random integers from 1 to 10
matrix = np.random.randint(1, 10, (4, 4))  # 1 and 10 are the bounds, parenthetical (4,4) is the matrix construction
print(matrix)  # Returns the randomly-filled 4x4 matrix

# Extracting single rows from a matrix is similar to extracting single elements from a list
print(matrix[0])  # Returns the first row of the matrix, at index 0
print(matrix[1])  # Returns the second row of the matrix, at index 1
print(matrix[-1])  # Returns the last row of the matrix using the '-1' trick - works for lists, too

# Extracting single elements from a matrix requires providing a row and column position based on index values
# Let's extract the second element of the first row
print(matrix[0][1])  # The parameters are [row index position] [column index position]
# Row index zero goes to the first row, column index 1 goes to the second column

# You can also change the values of specific rows or elements in a matrix
# Changing the elements in an entire row
matrix[1] = 0  # Set all element in row 2 (index 1) equal to zero
print(matrix)
# Changing a specific element
matrix[0][2] = 8  # Set the third element in the first row equal to 8
print(matrix)  # Note the single changed value