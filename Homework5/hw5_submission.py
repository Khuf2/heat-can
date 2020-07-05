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
        return None

    # Use a for-each type for loop to access the elements from list.
    def eachPrint(list):
        # Your code here
        return None
    
    # Stop here
    return (eachPrint(list) == rangePrint(list))

# You want this to equal true, where you recreate the same list two ways.
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
    return None
    
print ( printTri(5) )

'''
# golfScore()
# Calculates golf score compared to the par for the course. Positive numbers (over-par) are returned as a string
# For example, +1 or -1 or 0
# Return a string of the score, either positive, negative, or zero.
'''
def golfScore(scorecard):
    # Grabs the sublists in scorecard, pars for the course and the golfer's score
    pars = scorecard[0]
    score = scorecard[1]
    if (len(pars) != len(score)):
        return "error"
    # Your code starts here.
    return None

# sample scorecard composed of two lists, pars for the course, and the golfer's score on each hole
# (+4)
earl_cal_club = [ [5, 4, 4, 5, 4, 3, 4, 3, 4], [5, 5, 3, 4, 7, 4, 6, 2, 4] ]

print ( golfScore(earl_cal_club) )