import numpy as np
import pandas as pd
import lxml

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

# It is possible to select elements of a matrix using conditional logic - we call this 'conditional selection'
# Start by creating a 5x5 matrix filled with random integers between 1 and 10
matrix = np.random.randint(1, 10, (5, 5))
print(matrix)  # THe matrix appears as expected
# Now we'll select only the elements in the matrix with a value greater than 7 and store them in a new array
new_matrix = matrix[matrix > 7]  # Note the use of square brackets rather than parentheses
print(new_matrix)  # Returns a single line of values greater than 7
# Here's how you'd select only the odd numbers within the matrix
# We'll need to use modulo and the == comparative operator
odd_matrix = matrix[matrix % 2 == 1]  # If the remainder of each element when divided by 2 is 1, it's an odd number
print(odd_matrix)
# Now we'll fetch the even numbers
even_matrix = matrix[matrix % 2 != 1]  # If the remainder of each number when divided by 2 is NOT 1, it's an even number
print(even_matrix)

# You can also use similar code to perform conditional *changes* to matrix content
# For example, replacing all negative numbers in a matrix with zeroes and all odd numbers with -2s
matrix = np.array([[2, 4, 6, 8], [-2, -4, -6, -8], [1, 3, 5, 7]])
print(matrix)  # Appears as expected
matrix[matrix < 0] = 0  # Replace all elements with values less than zero with zeroes
print(matrix)  # All negative values in row two are now zeroes
matrix[matrix % 2 == 1] = -2  # Replace all odd numbers (see line 153) with -2s
print(matrix)  # All odd numbers in row three are now -2s

# Moving to pandas!
# Pandas is a data manipulation-and-analysis library that is built 'on top of' numpy
# It uses a data structure called a dataframe - think of it as invisible, 'floating' Excel but in Python
# Using dataframes mean we can store data in tabular form, i.e. in rows and columns
# A 'series' is a term you'll hear used that basically means 'a single column of a dataframe'
# You can create dataframes out of Python dictionaries, .csv files, HTML files, etc.

# Dataframes can be created and filled manually
# As an example, let's create a tiny fake bank client database
# You'll note that a lot of this code is similar to manual definition of a standard Python dictionary
bank_client_df = pd.DataFrame({'Bank Client ID': [111, 222, 333, 444],
                              'Bank Client Name': ['Chanel', 'Steve', 'Mitch', 'Ryan'],
                              'Net Worth [$]': [3500, 29000, 10000, 2000],
                              'Years with Bank': [3, 4, 9, 5]})
# Now we've defined the column headers and the associated values for each row. Entry order matters here, obviously
print(bank_client_df)  # This now looks like a small Excel table
print(type(bank_client_df))  # Returns a type of 'pandas.core.frame.DataFrame'

# By using the head() and tail() functions and passing numbers as parameters, you can select the Q first or last rows
print(bank_client_df.head(2))  # Returns the first two rows of the dataframe
print(bank_client_df.tail(2))  # Returns the last two rows of the dataframe

# You can run calculations based on information in a dataframe
# For example, a dataframe containing a stock portfolio
# We'll define a dataframe with three stocks, the number of shares held, and the price per share
# Then, we'll calculate the total value of the portfolio
portfolio = pd.DataFrame({'Stock Symbol': ['AAPL', 'GMC', 'RIVN'],
                          'Stock Name': ['Apple Computer', 'General Motors Corporation', 'Rivian Automotive'],
                          'Shares Held': [150, 225, 60],
                          'Price per Share': [167.23, 38.56, 32.21]})
print(portfolio)  # Prints as expected
# Now let's calculate the total value of the portfolio
total_dollar_value = portfolio['Price per Share'] * portfolio['Shares Held']  # Multiplying at the row-by-column level
print(total_dollar_value)  # Returns the results of each number of shares multiplied by each stock's price
print(total_dollar_value.sum())  # The sum() function adds up each of those three calculations to give the total value

# Pandas also has the capability to read HTML data and store the results in a dataframe
# You obviously need a website with a table on it
# You also need to import the lxml package or this won't work
house_price_df = pd.read_html('https://www.livingin-canada.com/house-prices-canada.html')  # Here's the URL we want
print(house_price_df[0])  # This will return the first table on the page
print(house_price_df[1])  # Here's the other table

# You can also use pandas to read .csv files
friends_table = pd.read_csv('C:/Users/doncs/Documents/TestData.csv')  # Passing a filepath for a .csv file I made
print(friends_table)  # And here's the table as we'd expect to see it in Excel

# Here's how to select only specific rows from a dataframe
# We'll use the friends table and select only the people older than 34
print(friends_table[friends_table['Age'] > 34])  # Indexing to the dataframe, then the column, then filtering

# Here's how to delete columns from a dataframe
del friends_table['Married']
print(friends_table)  # The 'Married' column is now gone

# You can also perform mathematical operations on columns directly
# Here's how to sum the ages of all the friends
print(friends_table['Age'].sum())  # Returns 346 using the .sum() function
