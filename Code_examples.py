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

# Let's try a small integration
# We will create a 1x10 array of random integers ranging from 0 to 'x,' where x is a value input by the user
upper_bound_raw = input('Enter the upper-boundary integer: ')  # Start by getting the user's input
# Per best-practices, we'll have a try/except to make sure the user didn't mess up
try:
    upper_bound = int(upper_bound_raw)  # See if we can re-type the input as an integer
except:  # If not:
    print('ERROR: Not an integer')  # Send an error message
    quit()  # And quit the program
defined_values = np.random.randint(0, upper_bound, 10)  # Otherwise, pass the numpy method the input integer as a bound
print(defined_values)  # And print the array of random integers
