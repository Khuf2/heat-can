# Homework 3 - 6/20/20
# Lists, Loops, Conditionals

# Testing:
# Modify the tets calls below each function for early testing. Then, in Terminal, simply type:
# python hw3_submission.py

# Final Scoring:
# When you finish, navigate to your code directory in Terminal and run with python hw3_tests.py
# This uses your code in this file and prints test results.

# The list you will use for your testing is this one here:
list = [2, 4, 6, 8, 10]

# (Medium) Write the code for two functions, swap() and manualReverse().

# swap()
# In a list, swaps the value at index a with the value at index b. 
# Hint: Dont let me make an IndexError. If a or b is outside of the array, return "Error"
def swap(list, a, b):
    # Your code starts here.
    if( ( abs(a) < len(list) ) and (abs(b) < len(list))):
        list[a], list[b] = list[b], list[a]
        # optional return of the list for good practice
        return list
    # implicit else
    return "Error"


# manualReverse() 
# Reverses the values in an array.
# You are NOT allowed to use reverse().
# Hint: You can use your swap method from above, i.e. swap(list, a, b).
# Hint 2: I found int() to be useful for making sure the array index is an integer.
def manualReverse(list):
    # Your code starts here
    for x in range(0, int(len(list)/2)):
        swap(list, x, int(len(list)-x-1))
    # optional return of the list for good practice
    return list


