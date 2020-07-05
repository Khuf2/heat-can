# Homework 2 - 6/19/20
# Lists, Loops, Conditionals

# Testing:
# Modify the tets calls below each function for early testing. Then, in Terminal, simply type:
# python hw2_submission.py

# Final Scoring:
# When you finish, navigate to your code directory in Terminal and run with python hw2_tests.py
# This uses your code in this file and prints test results.

# The list you will use for your testing is this one here:
numList = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
wordList = ["hmm", "why", "does", "it", "smell", "like", "burnt", "toast", "here"]
mixedList = ["going", 2, "raise", 8, "baby", "geese"]

# (Easy) Write the code for two functions, manualAbs() and smartAdd().

# manualAbs()
# Takes a number num, and returns the absolute value.
# For this question, you are NOT allowed to use the pre-existing abs() function.
# Hint: Use if statements.
def manualAbs(num):
    # Your code starts here. 
    return None

# Test call to the function.
print ( manualAbs(-40) )


# sumList() 
# Adds the values of all values in a list, and returns that sum.
# Hint: Use a loop.
def sumList(list):
    # Your code starts here
    # list = numList by my default setup.
    return None

# Test call to the function.
print ( sumList(numList) )



# (Medium) Write the code for the function, cutShort().

# cutShort()

# Part 1 - Build it to work for a list of strings
# Create a new list of all the words in wordList with length greater than n.
# Finish by returning the new list. Don't modify the old list.
# Hint: The length of a string can be found with len(<your string>)
def cutShort(list, n):
    # Your code starts here 
    return None

print ( cutShort(wordList, 3) )

# Part 2 - Modify the above function to work for a mixed list of both strings and integers, 
# where integers less than or equal to n are cut.
# Hint: Use if statements and this resource:
# https://www.w3schools.com/python/ref_func_isinstance.asp

# print ( cutShort(mixedList, 3))