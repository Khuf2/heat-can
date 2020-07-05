# Homework 5 - 6/24/20
# Lists, Nested Loops, For Loop Review and Practice

# Terminal commands:
# python hw5_tests.py
# or 
# python hw5_submission.py

# Blitz Problem: for loops
'''
# This is a two part problem. Build a for loop two different ways to output the same list. If they are the same, it succeeds.
# For both, create a new list and add each element from list into a new list with a for loop. Then return the new list.
'''
def blitz():
    # Original list
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Use a for loop, accessing the elements from list by their index.
    def rangePrint(list):
        # Your code here
        newList = []
        for x in range(0, len(list)):
            newList.append(list[x])
        return newList

    # Use a for-each type for loop to access the elements from list.
    def eachPrint(list):
        # Your code here
        newList = []
        for x in list:
            newList.append(x)
        return newList

    return (eachPrint(list) == rangePrint(list))

print ( blitz() )

# (Medium) Write the code for two functions, swap() and manualReverse().
'''
# printTri()
# Returns a string, which looks like a triangle made of "*" chars, with dimension height.
# Ex: height = 5
# *
# **
# ***
# ****
# *****
# Hint: This requires a nested for loop.
# Hint 2: Add a "\n" char after each line. This is equivalent to pressing Enter.
'''
def printTri(height):
    # Your code starts here.
    line = ""
    for y in range(0, height):
        for x in range(0, y+1):
            line += "*"
        line += '\n'
    return line
    
print ( printTri(5) )

'''
# But what happens if we have a list, and in each index of the list, is another list?
# This creates a 2-D array, or a n x m matrix, where n and m are the lengths of the lists.

# For this problem, I've started the matrix for you, but its empty.
# I want you to check to see if my matrix is the identity matrix, which looks like this:
# n = 3:
# [1] [0] [0]
# [0] [1] [0]
# [0] [0] [1]
# Return False once you know the matrix is not an identity matrix.
# If there are no errors and the matrix is valid, return True
'''
def golfScore(scorecard):
    pars = scorecard[0]
    score = scorecard[1]
    if (len(pars) != len(score)):
        return "error"
    # Your code starts here.
    overUnder = 0
    for x in range(0, len(pars)):
        overUnder += (score[x]-pars[x])
    if overUnder > 0:
        output = "+" + str(overUnder)
    else: 
        output = str(overUnder)
    return output

# sample scorecard composed of two lists, pars for the course, and the golfer's score on each hole
# (+4)
earl_cal_club = [ [5, 4, 4, 5, 4, 3, 4, 3, 4], [5, 5, 3, 4, 7, 4, 6, 2, 4] ]

print ( golfScore(earl_cal_club) )